# app/tts_service.py
from tempfile import NamedTemporaryFile

from elevenlabs.client import ElevenLabs

from .config import settings


class TTSService:
    def __init__(self):
        self.client = ElevenLabs(api_key=settings.ELEVEN_API_KEY)

    def text_to_audio(self, text: str) -> bytes:
        audio_gen = self.client.generate(
            text=text, voice="Brian", model="eleven_multilingual_v2"
        )
        with NamedTemporaryFile(delete=True, suffix=".mp3") as temp_audio_file:
            for chunk in audio_gen:
                temp_audio_file.write(chunk)
            temp_audio_file.flush()
            return temp_audio_file.read()


tts_service = TTSService()
