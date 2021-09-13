.PHONY: install update clean build run debug test style
PACKAGE := $(shell grep name pyproject.toml -m1 | awk -F" " '{print $$3}')
VERSION := $(shell grep version pyproject.toml -m1 | awk -F" " '{print $$3}')

install:
	poetry install
	poetry run pre-commit install

update:
	poetry update
	poetry run pre-commit autoupdate

clean:
	rm -rf dist

build: clean
	poetry build

run:
	poetry run ${PACKAGE}

debug:
	poetry run pytest ./tests -s -v --cov=pypj --cov-branch --durations=0

test:
	poetry run tox

style:
	poetry run tox -e black,flake8,mypy,isort
