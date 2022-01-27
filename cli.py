#!/usr/bin/env python3

import asyncio
from functools import wraps

import click

from app import http, openai


def coroutine(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))

    return wrapper


@click.group()
def cli():
    pass


@cli.command()
@click.argument("question")
@coroutine
async def ask(question):
    answer = await openai.ask(question)
    print(answer)


if __name__ == "__main__":
    http.client.init()
    cli()
