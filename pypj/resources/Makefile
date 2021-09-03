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