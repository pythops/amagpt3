import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "34xULHbQt4Ns6P29KsWhX4SRm7rypJyxhFL")

    OPENAI_URL = "https://api.openai.com/v1/answers"
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "curie")

    SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
    SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")


config = Config()
