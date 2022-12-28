.PHONY: install update clean build run debug test
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
	poetry run pytest ./tests -s -v -x --cov=pypj --cov-branch --durations=0 -l

test:
	poetry run tox

quickcheck:
	poetry run pytest ./tests -x --picked -l

unittest:
	poetry run tox -e py38,py39,py310

style:
	poetry run tox -e black,flake8,mypy,isort

format:
	poetry run tox -e black,isort

lint:
	poetry run tox -e flake8

type:
	portry run tox -e mypy
