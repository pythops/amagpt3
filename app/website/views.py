from quart import Blueprint, render_template

from app import openai
from app.website.forms import QuestionForm

website = Blueprint("website", __name__)


@website.route("/", methods=["GET", "POST"])
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
