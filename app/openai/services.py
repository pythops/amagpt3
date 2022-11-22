from app import http
from app.config import config
from app.openai import serializers


async def ask(question):
    url = config.OPENAI_URL
    headers = {"Authorization": f"Bearer {config.OPENAI_API_KEY}"}
    body = {
        "prompt": question,
        "model": config.OPENAI_MODEL,
        "temperature": config.OPENAI_MODEL_AUDACITY,
        "max_tokens": config.OPENAI_MAX_TOKEN,
    }
    response = await http.client.post(url, headers=headers, body=body)

    answer = serializers.OpenaiResponseSerializer().dump(response)["answer"]
    return answer
