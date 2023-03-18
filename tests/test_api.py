import pytest

from app.config import config


@pytest.mark.asyncio
async def test_ask(httpx_mock, openai_response, api):
    httpx_mock.add_response(url=config.OPENAI_URL, json=openai_response)

    body = {"question": "A question"}
    response = await api.post("ask", json=body)
    response_body = await response.json

    assert response.status_code == 200
    assert response_body == {
        "answer": "The biggest black hole in the universe is currently believed to be TON 618, which is located about 10.4 billion light-years away from Earth. It has a mass estimated to be around 66 billion times that of the sun. However, there may be even larger black holes that have not yet been discovered."
    }
