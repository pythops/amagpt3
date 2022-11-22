from click.testing import CliRunner

from cli import cli

from app.config import config


def test_cli(httpx_mock, openai_response):
    httpx_mock.add_response(url=config.OPENAI_URL, json=openai_response)
    runner = CliRunner()
    result = runner.invoke(cli, ["ask", "A question"])
    assert result.exit_code == 0
    assert result.output == "An answer...\n"
