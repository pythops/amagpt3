import re

from marshmallow import Schema, fields


class OpenaiResponseSerializer(Schema):
    answer = fields.Method("get_answer")

    def get_answer(self, data):
        answer = ""
        for choice in data["choices"]:
            answer += re.sub("[\n?]+", "", choice["text"])
        answer += "..."
        return answer
