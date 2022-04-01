from quart import Blueprint

from app.api.utils import response

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(401)
async def http_401(exception):
    message = {"description": "Unauthorized"}
    return await response(message, 401)


@errors.app_errorhandler(404)
async def http_404(exception):
    message = {"description": "Requested url not found"}
    return await response(message, 404)


@errors.app_errorhandler(405)
async def http_405(exception):
    message = {"description": "Method Not allowed"}
    return await response(message, 405)


@errors.app_errorhandler(422)
async def http_422(exception):
    message = {
        "description": "Unprocessable entity",
        "content": {"message": exception.exc.messages},
    }
    return await response(message, 422)


@errors.app_errorhandler(429)
async def http_429(exception):
    message = {"description": "Too many requests"}
    return await response(message, 429)


@errors.app_errorhandler(500)
async def http_500(exception):
    message = {"description": "Internal server error"}
    return await response(message, 500)
