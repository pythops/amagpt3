import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "34xULHbQt4Ns6P29KsWhX4SRm7rypJyxhFL")

    OPENAI_URL = "https://api.openai.com/v1/completions"
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "text-babbage-001")
    OPENAI_MODEL_AUDACITY = float(os.getenv("OPENAI_MODEL_AUDACITY", 0))
    OPENAI_MAX_TOKEN = int(os.getenv("OPENAI_MAX_TOKEN", 25))

    QUESTION_MAX_CHAR = int(os.getenv("QUESTION_MAX_CHAR", 100))

    SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
    SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")


config = Config()
