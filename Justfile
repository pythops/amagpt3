default:
    @just --list

#
# API
#

setup-api:
    #!/usr/bin/env bash
    python3 -m venv .venv &&
    source .venv/bin/activate &&
    pip3 install -U pip &&
    pip3 install -r requirements/common.txt

run-api:
    #!/usr/bin/env bash
    source .venv/bin/activate &&
    hypercorn --access-logfile - --error-logfile - run-api:api --reload

build-api:
    buildah build -f Containerfile.api -t amagpt3:api .

deploy-api:
    podman run -d -e OPENAI_API_KEY=$OPENAI_API_KEY -p 8000:8000 amagpt3:api

#
# Website
#

setup-website:
    #!/usr/bin/env bash
    python3 -m venv .venv &&
    source .venv/bin/activate &&
    pip3 install -U pip &&
    pip3 install -r requirements/common.txt &&
    pip3 install -r requirements/website.txt

run-website:
    #!/usr/bin/env bash
    source .venv/bin/activate &&
    hypercorn --access-logfile - --error-logfile - run-website:website --reload

build-website:
    buildah build -f Containerfile.website -t amagpt3:website .

deploy-website:
    podman run -d -e OPENAI_API_KEY=$OPENAI_API_KEY -p 8000:8000 amagpt3:website

#
# Slack
#

setup-slack:
    #!/usr/bin/env bash
    python3 -m venv .venv &&
    source .venv/bin/activate &&
    pip3 install -U pip &&
    pip3 install -r requirements/common.txt &&
    pip3 install -r requirements/slack.txt

run-slack:
    #!/usr/bin/env bash
    source .venv/bin/activate &&
    python slack.py

build-slack:
    buildah build -f Containerfile.slack -t amagpt3:slack .

deploy-slack:
    podman run -d \
        -e OPENAI_API_KEY=$OPENAI_API_KEY \
        -e SLACK_APP_TOKEN=$SLACK_APP_TOKEN \
        -e SLACK_BOT_TOKEN=$SLACK_BOT_TOKEN \
        amagpt3:slack

#
# Cli
#

setup-cli:
    #!/usr/bin/env bash
    python3 -m venv .venv &&
    source .venv/bin/activate &&
    pip3 install -U pip &&
    pip3 install -r requirements/common.txt &&
    pip3 install -r requirements/cli.txt

#
# Dev
#

dev:
    #!/usr/bin/env bash
    python3 -m venv .venv &&
    source .venv/bin/activate &&
    pip3 install -U pip &&
    pip3 install -r requirements/common.txt &&
    pip3 install -r requirements/cli.txt &&
    pip3 install -r requirements/website.txt &&
    pip3 install -r requirements/dev.txt &&
    pip3 install -r requirements/slack.txt &&
    pip3 install -r requirements/test.txt

pip-update:
    #!/usr/bin/env bash
    pip-compile --output-file=requirements/common.txt -U requirements/common.in --resolver=backtracking &&
    pip-compile --output-file=requirements/cli.txt -U requirements/cli.in --resolver=backtracking &&
    pip-compile --output-file=requirements/website.txt -U requirements/website.in --resolver=backtracking &&
    pip-compile --output-file=requirements/dev.txt -U requirements/dev.in --resolver=backtracking &&
    pip-compile --output-file=requirements/slack.txt -U requirements/slack.in --resolver=backtracking &&
    pip-compile --output-file=requirements/test.txt -U requirements/test.in --resolver=backtracking

#
# Test
#

test:
    #!/usr/bin/env bash
    source .venv/bin/activate &&
    flake8 &&
    pytest tests --cov app/
