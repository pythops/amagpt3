from app import http
from app.config import config
from app.openai import serializers


async def ask(question):
    url = config.OPENAI_URL
    headers = {"Authorization": f"Bearer {config.OPENAI_API_KEY}"}
    body = {
        "question": question,
        "model": config.OPENAI_MODEL,
        "documents": [],
        "examples_context": "",
        "examples": [
            ["What is human life expectancy in the United States?", "78 years."]
        ],
    }
    response = await http.client.post(url, headers=headers, body=body)

    answer = serializers.OpenaiResponseSerializer().dump(response)
    return answer
