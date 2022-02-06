from marshmallow import Schema, fields, validate


class QuestionSchema(Schema):
    question = fields.Str(validate=validate.Length(30))
