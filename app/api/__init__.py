import quart.flask_patch  # noqa
from quart import Quart

from app import http


def init_api():
    server = Quart(__name__)
    http.client.init()

    from app.api.views import api

    server.register_blueprint(api)

    return server
