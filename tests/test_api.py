import pytest

from app.config import config


@pytest.mark.asyncio
async def test_ask(httpx_mock, openai_response, api):
    httpx_mock.add_response(url=config.OPENAI_URL, json=openai_response)

    body = {"question": "A question"}
    response = await api.post("ask", json=body)
    response_body = await response.json

    assert response.status_code == 200
    assert response_body == {"answer": "An answer..."}
