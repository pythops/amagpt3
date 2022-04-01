from datetime import timedelta

from quart import Blueprint
from quart_rate_limiter import rate_limit
from webargs.flaskparser import use_kwargs

from app.api import controllers, schemas
from app.api.utils import response

api = Blueprint("api", __name__)


@api.route("/ask", methods=["POST"])
@use_kwargs(schemas.QuestionSchema())
@rate_limit(1, timedelta(seconds=1))
async def ask(question):
    answer = await controllers.ask(question)
    return await response({"answer": answer}, 200)
