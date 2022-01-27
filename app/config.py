import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "34xULHbQt4Ns6P29KsWhX4SRm7rypJyxhFL")
    OPENAI_URL = "https://api.openai.com/v1/answers"
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "curie")


config = Config()
