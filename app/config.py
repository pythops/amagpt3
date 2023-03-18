import os
import secrets


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_urlsafe(32))

    OPENAI_URL = "https://api.openai.com/v1/chat/completions"
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    OPENAI_MODEL_AUDACITY = float(os.getenv("OPENAI_MODEL_AUDACITY", 0))
    OPENAI_MAX_TOKEN = int(os.getenv("OPENAI_MAX_TOKEN", 100))

    QUESTION_MAX_CHAR = int(os.getenv("QUESTION_MAX_CHAR", 200))

    SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
    SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")


config = Config()
