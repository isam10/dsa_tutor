import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    DATABASE_PATH = os.getenv("DATABASE_PATH", "dsa_tutor.db")


