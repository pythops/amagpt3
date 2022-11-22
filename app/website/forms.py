from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, length

from app.config import config


class QuestionForm(FlaskForm):
    question = StringField(
        "question", validators=[DataRequired(), length(max=config.QUESTION_MAX_CHAR)]
    )
