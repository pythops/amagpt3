import httpx


class HttpClient:
    def __init__(self):
        self.client = None

    def init(self):
        self.client = httpx.AsyncClient()

    async def post(self, url, headers, body):
        r = await self.client.post(url, headers=headers, json=body)
        return r.json()


client = HttpClient()
