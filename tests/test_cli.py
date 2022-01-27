from click.testing import CliRunner

from cli import cli

from app.config import config


def test_cli(httpx_mock):
    httpx_mock.add_response(url=config.OPENAI_URL, json={"answers": ["An answer"]})
    runner = CliRunner()
    result = runner.invoke(cli, ["ask", "A question"])
    assert result.exit_code == 0
    assert result.output == "An answer\n"
