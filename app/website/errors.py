import quart.flask_patch  # noqa
from flask_wtf.csrf import CSRFError
from quart import Blueprint, redirect, render_template, request

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(404)
async def error_404(error):
    return await render_template("errors/404.html", title="Not Found"), 404


@errors.app_errorhandler(405)
async def error_405(error):
    return await render_template("errors/405.html", title="Not Allowed"), 405


@errors.app_errorhandler(403)
async def error_403(error):
    return await render_template("errors/403.html", title="Unauthorized Access"), 403


@errors.app_errorhandler(429)
async def error_429(error):
    return await render_template("errors/429.html", title="Too many requests"), 429


@errors.app_errorhandler(500)
async def error_500(error):
    return await render_template("errors/500.html", title="Server Error"), 500


@errors.app_errorhandler(CSRFError)
async def error_CSRF(error):
    return redirect(request.url)
