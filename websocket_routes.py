import json
import os

from fastapi import WebSocket, WebSocketDisconnect

from services.avatar_animation import generate_clip, get_video
from services.llm_service import llm_service
from services.stt_service import save_audio_to_temp_file, speech_to_text
from services.tts_service import tts_service


async def conversation_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Receive data from client
            request_data = await websocket.receive_text()
            data = json.loads(request_data)

            session_id = data.get("session_id")
            if not session_id:
                await websocket.send_text(json.dumps({"error": "Missing session_id"}))
                break

            # Check if the request contains text or audio
            if "prompt" in data:

                prompt = data.get("prompt")

                # Generate LLM response with stateful chat history
                response_text = llm_service.generate_response(prompt, session_id)
                await websocket.send_text(json.dumps({"text": response_text}))

                # Generate avatar clip for AI response
                avatar_clip_id = generate_clip(response_text)
                video_url = get_video(avatar_clip_id)
                await websocket.send_text(json.dumps({"video_url": video_url}))

                # Convert response text to audio
                # audio_bytes = tts_service.text_to_audio(response_text)
                # await websocket.send_bytes(audio_bytes)

            elif "audio" in data:
                # Audio processing logic
                audio_data = data.get("audio")
                if not audio_data:
                    await websocket.send_text(
                        json.dumps({"text": "Audio data is empty"})
                    )
                    continue

                # Save the audio to a temporary file
                temp_file_path = save_audio_to_temp_file(audio_data)
                # Transcribe the audio
                transcribed_text = speech_to_text(temp_file_path)
                # Remove the temporary audio file
                os.remove(temp_file_path)

                # Generate LLM response for transcribed audio
                response_text = llm_service.generate_response(
                    transcribed_text, session_id
                )
                await websocket.send_text(json.dumps({"text": response_text}))

                # Generate avatar clip for AI response
                avatar_clip_id = generate_clip(response_text)
                video_url = get_video(avatar_clip_id)
                await websocket.send_text(json.dumps({"video_url": video_url}))

            else:
                # Case where neither text nor audio is provided
                await websocket.send_text(
                    json.dumps({"text": "Invalid request: expected text or audio data"})
                )

    except WebSocketDisconnect:
        print("Client disconnected")
