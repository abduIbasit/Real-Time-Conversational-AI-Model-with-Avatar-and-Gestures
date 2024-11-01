import json
import os

from fastapi import WebSocket, WebSocketDisconnect

from services.avatar_animation import avatar_animation
from services.llm_service import llm_service
from services.stt_service import stt_service
from services.tts_service import tts_service


async def conversation_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Receive data from client
            request_data = await websocket.receive_text()
            data = json.loads(request_data)

            # Retrieve session_id from request parameter to track chat history
            session_id = data.get("session_id")
            if not session_id:
                await websocket.send_text(json.dumps({"error": "Missing session_id"}))
                continue

            # Check if the request contains text or audio(voice recording)
            if "prompt" in data:

                prompt = data.get("prompt")

                # Generate LLM response with stateful chat history
                response_text = llm_service.generate_response(prompt, session_id)
                await websocket.send_text(json.dumps({"text": response_text}))

                # Generate avatar clip for AI response
                avatar_clip_id = avatar_animation.generate_clip(response_text)
                # Poll video generation and send the url to the client when ready
                video_url = avatar_animation.get_video(avatar_clip_id)
                await websocket.send_text(json.dumps({"video_url": video_url}))

            # Process audio/voice recording
            elif "audio" in data:

                audio_data = data.get("audio")

                # Decode base64 voice recording from client and save to a temporary file
                temp_file_path = stt_service.save_audio_to_temp_file(audio_data)
                # Transcribe the audio
                transcribed_text = stt_service.speech_to_text(temp_file_path)
                # Remove the temporary audio file
                os.remove(temp_file_path)

                # Generate LLM response for transcribed audio
                response_text = llm_service.generate_response(
                    transcribed_text, session_id
                )
                await websocket.send_text(json.dumps({"text": response_text}))

                # Generate avatar clip for AI response
                avatar_clip_id = avatar_animation.generate_clip(response_text)
                video_url = avatar_animation.get_video(avatar_clip_id)
                await websocket.send_text(json.dumps({"video_url": video_url}))

            else:
                # Case where neither text nor audio is provided
                await websocket.send_text(
                    json.dumps(
                        {"error": "Invalid request: expected text or audio data"}
                    )
                )

    except WebSocketDisconnect:
        print("Client disconnected")
