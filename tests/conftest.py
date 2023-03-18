import pytest
import pytest_asyncio

from app.api import init_api
from app.website import init_website


@pytest.mark.asyncio
@pytest_asyncio.fixture
async def api():
    api = init_api()
    yield api.test_client()


@pytest.mark.asyncio
@pytest_asyncio.fixture
async def website():
    website = init_website()
    yield website.test_client()


@pytest.mark.asyncio
@pytest_asyncio.fixture
async def openai_response():
    return {
        "choices": [
            {
                "finish_reason": "stop",
                "index": 0,
                "message": {
                    "content": "The biggest black hole in the universe is currently believed to be TON 618, which is located about 10.4 billion light-years away from Earth. It has "
                    "a mass estimated to be around 66 billion times that of the sun. However, there may be even larger black holes that have not yet been discovered.",
                    "role": "assistant",
                },
            }
        ],
        "created": 1679143283,
        "id": "chatcmpl-6vQA7b6MWyfi8lGC723Np7v6CFO41",
        "model": "gpt-3.5-turbo-0301",
        "object": "chat.completion",
        "usage": {"completion_tokens": 66, "prompt_tokens": 28, "total_tokens": 94},
    }
