![Pypj Logo](https://raw.githubusercontent.com/edge-minato/pypj/main/doc/img/logo.png)

[![pypi version](https://img.shields.io/pypi/v/pypj.svg?style=flat)](https://pypi.org/pypi/pypj/)
[![python versions](https://img.shields.io/pypi/pyversions/pypj.svg?style=flat)](https://pypi.org/pypi/pypj/)
[![format](https://img.shields.io/pypi/format/pypj.svg?style=flat)](https://pypi.org/pypi/pypj/)
[![license](https://img.shields.io/pypi/l/pypj.svg?style=flat)](https://github.com/edge-minato/pypj/blob/master/LICENSE)
[![Unittest](https://github.com/edge-minato/pypj/actions/workflows/unittest.yml/badge.svg)](https://github.com/edge-minato/pypj/actions/workflows/unittest.yml)
[![codecov](https://codecov.io/gh/edge-minato/pypj/branch/main/graph/badge.svg?token=YDZAMKUNS0)](https://codecov.io/gh/edge-minato/pypj)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black")
[![Downloads](https://img.shields.io/pypi/dm/fbm.svg)](https://pypistats.org/packages/pypj)

`Pypj` provides you an initialized modern python project. All the basic dev package installations, their configurations, and test workflows will be done, so we can focus on coding. All you have to do is install `poetry` and hit `pypj`, name your project.

## What will be provided

The _"Modern"_ project settings `Pypj` suggests is following. We understand some developers prefer another tools, and you can remove or customize the packages to be installed.

### Environment

- Package manager: [`poetry`](https://github.com/python-poetry/poetry)
- Formatter: [`black`](https://github.com/psf/black)
- Linter: [`pflake8`](https://github.com/csachs/pyproject-flake8)
- Type linter: [`mypy`](https://github.com/python/mypy)
- Import formatter: [`isort`](https://github.com/PyCQA/isort)
- Test framework:
  - [`pytest`](https://github.com/pytest-dev/pytest)
    - [`pytest-cov`](https://github.com/pytest-dev/pytest-cov)
    - [`pytest-mock`](https://github.com/pytest-dev/pytest-mock)
  - [`tox`](https://github.com/tox-dev/tox)
    - [`tox-gh-actions`](https://github.com/ymyzk/tox-gh-actions)

### Coding format

- Max line length: `119` as default
- Type hinting: `required`
- And some detailed configures

### Other features

- Single filed configurations on `pyproject.toml`
- Single sourced versioning: [`single-source`](https://github.com/rabbit72/single-source)
- Command alias: [`make`](https://www.gnu.org/software/make/)
- CI/CD
  - unittest workflow

### Directory structure

Do you think the directory tree looks poor? Because all configurations are aggregated in `pyproject.toml`, we don't need any tool specific configuration files.

```
$ tree -a -L 1
my-package/
├── .github
├── .pre-commit-config.yaml
├── .venv
├── .vscode
├── Makefile
├── README.md
├── my-package
├── poetry.lock
├── pyproject.toml
└── tests
```

## Requirements

- `python3`
- `poetry` [[Installation guide](https://python-poetry.org/docs/#installation)]

## Installation

```sh
pip install pypj
```

## Usage

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
pytest-cov = "^2.12.1"

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
    | venv
)
'''

[tool.flake8]
max-line-length = 119
max-complexity = 10

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
```

## Supported python versions

- Supported: `3.7`, `3.8`, `3.9`
- Is going to be supported: `3.10`
- Not supported: `3.6` or less

**NOTE**: According to [Status of Python branches](https://devguide.python.org/#status-of-python-branches), the EoL of Python 3.6 is `2021-12-23`.
