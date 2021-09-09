.PHONY: install test clean build run
PACKAGE := $(shell grep name pyproject.toml -m1 | awk -F" " '{print $$3}')
VERSION := $(shell grep version pyproject.toml -m1 | awk -F" " '{print $$3}')

install:
	poetry install

test:
	poetry run tox

clean:
	rm -rf dist

build: clean
	poetry build

run:
	poetry run ${PACKAGE}

debug:
	poetry run pytest ./tests -s -v --cov=pypj --cov-branch --durations=0

unittest:
	poetry run tox -e py37,py38,py39
