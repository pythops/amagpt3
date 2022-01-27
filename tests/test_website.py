import pytest


@pytest.mark.asyncio
async def test_home(website):
    response = await website.get("/")

    assert response.status_code == 200
