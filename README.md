![pypj Logo](https://raw.githubusercontent.com/edge-minato/pypj/main/doc/img/logo.png)

[![pypi version](https://img.shields.io/pypi/v/pypj.svg?style=flat)](https://pypi.org/pypi/pypj/)
[![python versions](https://img.shields.io/pypi/pyversions/pypj.svg?style=flat)](https://pypi.org/pypi/pypj/)
[![license](https://img.shields.io/pypi/l/pypj.svg?style=flat)](https://github.com/edge-minato/pypj/blob/master/LICENSE)
[![Unittest](https://github.com/edge-minato/pypj/actions/workflows/unittest.yml/badge.svg)](https://github.com/edge-minato/pypj/actions/workflows/unittest.yml)
[![codecov](https://codecov.io/gh/edge-minato/pypj/branch/main/graph/badge.svg?token=YDZAMKUNS0)](https://codecov.io/gh/edge-minato/pypj)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black")
[![Downloads](https://pepy.tech/badge/pypj)](https://pepy.tech/project/pypj)
[![Downloads](https://pepy.tech/badge/pypj/week)](https://pepy.tech/project/pypj)

`pypj` provides you a modern python project template. All the basic dev package installations, their configurations, and test workflows will be done, so you can focus on coding.

## What will be provided

What the _"Modern"_ means is expressed as following directory structure. Some developers prefer another tools, and you can remove or customize the tools to be prepared. Most of all configurations regarding the code style tools, like formatter and linter, are aggregated in `pyproject.toml`.

```
my-package/
├── .github
│   ├── dependabot.yml       # Dependency updater
│   └── workflows
│       ├── publish.yml      # Tagging on GitHub triggers publishing to Pypi
│       └── unittest.yml     # On each push and PR, execute the unittest
├── .pre-commit-config.yaml  # Checks format and styles of each file
├── .venv                    # venv can be outside of project directory
├── .vscode
│   └── settings.json        # Format, Lint, Type check and Import sort on save
├── Makefile                 # Useful command alias
├── README.md                # How to start with pypj
├── my-package               # Your package, can be "src"
├── poetry.lock
├── pyproject.toml           # Configured settings
└── tests
```

## Developing tools pypj provides

- Package manager: [`poetry`](https://github.com/python-poetry/poetry)
- Formatter: [`black`](https://github.com/psf/black)
- Linter: [`pflake8`](https://github.com/csachs/pyproject-flake8) (\*1)
  - Plugin: [`flake8-bugbear`](https://github.com/PyCQA/flake8-bugbear)
- Type checker: [`mypy`](https://github.com/python/mypy)
- Import sorter: [`isort`](https://github.com/PyCQA/isort)
- Test framework:
  - [`pytest`](https://github.com/pytest-dev/pytest)
    - [`pytest-cov`](https://github.com/pytest-dev/pytest-cov)
    - [`pytest-mock`](https://github.com/pytest-dev/pytest-mock)
  - [`tox`](https://github.com/tox-dev/tox)
    - [`tox-gh-actions`](https://github.com/ymyzk/tox-gh-actions)
- Git hooks manager: [`pre-commit`](https://github.com/pre-commit/pre-commit)

(\*1) `pflake8` wraps `flake8` to aggregate settings to `pyproject.toml`

## Coding format pypj provides

- Max line length: `119` as default
- Type hinting: `required`
- And some detailed configurations

## Customize

Here is an actual interaction to customize.

```
Package name: my-package
Do you want to customize settings? (y/N): y
Max line length (119):
Use src directory (y/N):
Keep venv in project (Y/n):
Use github workflows (Y/n):
Use vscode settings (Y/n):
Use pre-commit (Y/n):
Use command alias as Makefile (Y/n):
Are you sure? (Y/n): y
```

## Other features

- Single filed configurations on `pyproject.toml`
- Single sourced versioning: [`single-source`](https://github.com/rabbit72/single-source)
- Command alias: [`make`](https://www.gnu.org/software/make/)
- CI/CD
  - unittest workflow
  - publish package workflow
  - dependency updater configuration

## Requirements

- `python3`
- `poetry` [[Installation guide](https://python-poetry.org/docs/#installation)]

## Installation

```sh
pip install pypj
```

## Usage

See also [README.md](pypj/resources/README.md) which will be generated with `pypj` command, it shows more actual usage.

```
$ pypj

┌─┐┬ ┬┌─┐┬
├─┘└┬┘├─┘│    python : 3.8.5
┴   ┴ ┴ └┘    poetry : 1.1.8

Package name: my-package
Do you want to customize settings? (y/N): N
Do you want to proceed? (y/N): y
Task: Initialize package: my-package
      Command: poetry new my-package ✨
      Poetry new done 🚀
      Command: poetry config virtualenvs.in-project true ✨
      Command: poetry add -D black ✨
      Command: poetry add -D pyproject-flake8 ✨
      Command: poetry add -D mypy ✨
      Command: poetry add -D isort ✨
      Command: poetry add -D pytest ✨
      Command: poetry add -D tox ✨
      Command: poetry add -D pytest-cov ✨
      Command: poetry add -D pytest-mock ✨
      Command: poetry add -D tox-gh-actions ✨
      Configure: __init__.py  ✨
      Create : my-package ✨
Task: Create README.md
      Create : README.md ✨
Task: Configure pyproject.toml settings
      Write  : pyproject.toml ✨
Task: Create github actions
      Create : unittest.yml ✨
      Create : publish.yml ✨
      Create : dependabot.yml ✨
Task: Configure vscode settings
      Create : .vscode/settings.json ✨
Task: Create makefile
      Create : Makefile ✨
Task: Configure pre-commit
      Create : .pre-commit-config.yaml ✨

Complete! 🚀
Let's make the world better! ✨😋🐍🌎
```

## Example configurations on `pyproject.toml`

With default setting, this kind of `pyproject.toml` file will be generated.

```toml
[tool.poetry]
name = "my-package"
version = "0.1.0"
description = ""
authors = ["you <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.8"

[tool.poetry.dev-dependencies]
pytest = "^5.2"
black = "^21.8b0"
pyproject-flake8 = "^0.0.1-alpha.2"
mypy = "^0.910"
isort = "^5.9.3"
tox = "^3.24.3"
pytest-cov = "^2.12.1"
pytest-mock = "^3.6.1"
tox-gh-actions = "^2.7.0"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.black]
line-length = 119
exclude = '''
(
    migrations
    | .mypy_cache
    | .pytest_cache
    | .tox
    | .venv
    | dist
)
'''

[tool.flake8]
max-line-length = 119
max-complexity = 10
select = "C,E,F,W,B"
ignore = "E203"

[tool.mypy]
# common
python_version = 3.8
show_column_numbers = true
show_error_context = true
ignore_missing_imports = true
check_untyped_defs = true
disallow_untyped_defs = true
# warning
warn_return_any = true
warn_unused_configs = true
warn_redundant_casts = true

[tool.isort]
profile = "black"
line_length = 119

[tool.tox]
legacy_tox_ini = """
[tox]
envlist = py38, flake8, black, mypy, isort
skipsdist = true
isolated_build = true
skip_missing_interpreters = true
[testenv]
whitelist_externals = poetry
require_locked_deps = true
install_dev_deps = true
commands =
    poetry install -vv --no-root
    pytest ./tests -v --cov=pypj --cov-branch --durations=0
[testenv:flake8]
commands = poetry run pflake8 ./my-package
[testenv:black]
commands = poetry run black ./my-package
[testenv:mypy]
commands = poetry run mypy ./my-package
[testenv:isort]
commands = poetry run isort ./my-package
"""
```

## Alias as Makefile

```Makefile
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
        poetry run ${PACKAGE} # Just in case the package provides a command

debug:
        poetry run pytest ./tests -s -v --cov=pypj --cov-branch --durations=0

test:
        poetry run tox

style:
        poetry run tox -e black,flake8,mypy,isort
```

## Supported python versions

- Supported: `3.7`, `3.8`, `3.9`
- Is going to be supported: `3.10`
- Not supported: `3.6` or less

**NOTE**: According to [Status of Python branches](https://devguide.python.org/#status-of-python-branches), the EoL of Python 3.6 is `2021-12-23`.


## FAQ

* Is there any restrictions regarding the package naming?
  * -> A name of python package is defined at [PEP-008 #Package and Module Names](https://www.python.org/dev/peps/pep-0008/#package-and-module-names) and it can be expressed as regex: `/^[a-zA-Z][0-9a-zA-Z\-_]*/`. `pypj` follows this rule.
