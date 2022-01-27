import pytest

from app.api import init_api
from app.website import init_website


@pytest.mark.asyncio
@pytest.fixture
async def api():
    api = init_api()
    yield api.test_client()


@pytest.mark.asyncio
@pytest.fixture
async def website():
    website = init_website()
    yield website.test_client()
