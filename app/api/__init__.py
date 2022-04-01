import quart.flask_patch  # noqa
from quart import Quart
from quart_rate_limiter import RateLimiter

from app import http

rate_limiter = RateLimiter()


def init_api():
    server = Quart(__name__)
    http.client.init()

    rate_limiter.init_app(server)

    from app.api.errors import errors
    from app.api.views import api

    server.register_blueprint(api)
    server.register_blueprint(errors)

    return server
