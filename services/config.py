# app/config.py
import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY", "")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
    LLM_MODEL_NAME = "llama3-8b-8192"
    DID_BEARER_TOKEN = os.getenv("DID_BEARER_TOKEN")


settings = Settings()
