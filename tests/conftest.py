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
        "id": "cmpl-6FKpO9OwNL7FVuEWdL1FTBSxhnPg7",
        "object": "text_completion",
        "created": 1669113002,
        "model": "text-babbage-001",
        "choices": [
            {
                "text": "?\n\nAn answer",
                "index": 0,
                "logprobs": None,
                "finish_reason": "length",
            }
        ],
        "usage": {"prompt_tokens": 5, "completion_tokens": 20, "total_tokens": 25},
    }
