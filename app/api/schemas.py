from marshmallow import Schema, fields, validate

from app.config import config


class QuestionSchema(Schema):
    question = fields.Str(validate=validate.Length(max=config.QUESTION_MAX_CHAR))
