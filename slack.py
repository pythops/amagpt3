from slack_bolt.adapter.socket_mode.async_handler import AsyncSocketModeHandler
from slack_bolt.app.async_app import AsyncApp

from app import http, openai
from app.config import config

app = AsyncApp(token=config.SLACK_BOT_TOKEN)


@app.command("/amagpt3")
async def slack_answer(ack, body, respond):
    await ack()
    question = body.get("text")
    answer = await openai.ask(question)
    response = (
        f"*Author:* <@{body['user_id']}>\n*Question:* {question}\n*Answer:* {answer}"
    )
    await respond(response, response_type="in_channel")


async def main():
    http.client.init()
    handler = AsyncSocketModeHandler(app, config.SLACK_APP_TOKEN)
    await handler.start_async()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
