from datetime import timedelta

from quart import Blueprint, render_template
from quart_rate_limiter import rate_limit

from app import openai
from app.website.forms import QuestionForm

website = Blueprint("website", __name__)


@website.route("/", methods=["GET", "POST"])
@rate_limit(3, timedelta(seconds=1))
async def home():
    form = QuestionForm()
    answer = ""
    question = ""
    if form.validate_on_submit():
        question = form.question.data
        answer = await openai.ask(question)
    return await render_template(
        "index.html", form=form, answer=answer, question=question
    )
