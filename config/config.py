import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY", "")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
    DID_BEARER_TOKEN = os.getenv("DID_BEARER_TOKEN")


settings = Settings()
