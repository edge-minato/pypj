.PHONY: install clean test build
PACKAGE := pypj

install:
	poetry install

test:
	poetry run tox

clean:
	rm -rf dist

build: clean
	poetry build

version-patch:
	poetry version patch

#test-publish:
#	poetry publish -r testpypi --username ${USER} --password ${PW}

#publish:
#	poetry publish --username ${USER} --password ${PW}