import base64

from groq import Groq

client = Groq()


def save_audio_to_temp_file(audio_data):
    """Decode base64 audio data and save it to a temporary .webm file"""
    decoded_audio = base64.b64decode(audio_data)
    temp_file_path = "temp_audio.webm"

    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(decoded_audio)

    return temp_file_path


def speech_to_text(audio_file_path):
    """Transcribe audio to text"""
    with open(audio_file_path, "rb") as file:
        transcription = client.audio.transcriptions.create(
            file=("audio.webm", file.read()),
            model="whisper-large-v3-turbo",
            response_format="verbose_json",
        )
        return transcription.text
