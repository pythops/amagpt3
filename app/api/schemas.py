from marshmallow import Schema, fields, validate


class QuestionSchema(Schema):
    question = fields.Str(validate=validate.Length(max=50))
