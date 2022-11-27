SHELL := /bin/bash

setup-api:
	@(\
	    python3 -m venv .venv && \
	    source .venv/bin/activate &&  \
	    pip3 install -U pip && \
	    pip3 install -r requirements/common.txt \
		)

setup-cli:
	@(\
	    python3 -m venv .venv && \
	    source .venv/bin/activate &&  \
	    pip3 install -U pip && \
	    pip3 install -r requirements/common.txt && \
	    pip3 install -r requirements/cli.txt \
		)

setup-website:
	@(\
	    python3 -m venv .venv && \
	    source .venv/bin/activate &&  \
	    pip3 install -U pip && \
	    pip3 install -r requirements/common.txt && \
	    pip3 install -r requirements/website.txt \
		)

setup-slack:
	@(\
	    python3 -m venv .venv && \
	    source .venv/bin/activate &&  \
	    pip3 install -U pip && \
	    pip3 install -r requirements/common.txt && \
	    pip3 install -r requirements/slack.txt \
		)

dev:
	@(\
	    python3 -m venv .venv && \
	    source .venv/bin/activate &&  \
	    pip3 install -U pip && \
	    pip3 install -r requirements/common.txt && \
	    pip3 install -r requirements/cli.txt && \
	    pip3 install -r requirements/website.txt && \
	    pip3 install -r requirements/dev.txt && \
	    pip3 install -r requirements/slack.txt && \
	    pip3 install -r requirements/test.txt \
		)

pip-update:
	@(\
      pip-compile --output-file=requirements/common.txt -U requirements/common.in --resolver=backtracking &&  \
      pip-compile --output-file=requirements/cli.txt -U requirements/cli.in --resolver=backtracking && \
      pip-compile --output-file=requirements/website.txt -U requirements/website.in --resolver=backtracking &&  \
      pip-compile --output-file=requirements/dev.txt -U requirements/dev.in --resolver=backtracking && \
      pip-compile --output-file=requirements/slack.txt -U requirements/slack.in --resolver=backtracking && \
      pip-compile --output-file=requirements/test.txt -U requirements/test.in --resolver=backtracking  \
		)

run-api:
	@(\
      source .venv/bin/activate && \
      hypercorn run-api:api --reload \
		)


run-website:
	@(\
      source .venv/bin/activate && \
      hypercorn --access-logfile - --error-logfile - run-website:website \
		)

run-slack:
	@(\
      source .venv/bin/activate && \
      python slack.py \
		)

test:
	@(\
      source .venv/bin/activate && \
      flake8 && \
      pytest tests --cov app/ \
		)
