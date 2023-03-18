from click.testing import CliRunner

from cli import cli

from app.config import config


def test_cli(httpx_mock, openai_response):
    httpx_mock.add_response(url=config.OPENAI_URL, json=openai_response)
    runner = CliRunner()
    result = runner.invoke(cli, ["ask", "A question"])
    assert result.exit_code == 0
    assert (
        result.output
        == "The biggest black hole in the universe is currently believed to be TON 618, which is located about 10.4 billion light-years away from Earth. It has a mass estimated to be around 66 billion times that of the sun. However, there may be even larger black holes that have not yet been discovered.\n"
    )
