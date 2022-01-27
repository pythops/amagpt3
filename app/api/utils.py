from quart import jsonify
from werkzeug.wrappers import Response


async def response(message: dict, status_code: int) -> Response:
    response = jsonify(message)
    response.status_code = status_code
    return response
