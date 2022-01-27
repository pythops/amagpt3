from marshmallow import Schema, fields, post_dump


class OpenaiResponseSerializer(Schema):
    answers = fields.List(fields.Str())

    @post_dump
    def postprocess(self, data, many, **kwargs):
        return " ".join(data["answers"])
