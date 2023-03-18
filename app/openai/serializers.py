from marshmallow import Schema, fields


class OpenaiResponseSerializer(Schema):
    answer = fields.Method("get_answer")

    def get_answer(self, data):
        return next(iter(data["choices"]))["message"]["content"]
