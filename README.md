```txt
┌─┐┬ ┬┌─┐┬
├─┘└┬┘├─┘│
┴   ┴ ┴ └┘
```

pypj is a command that initializes a modern python project.

## Installation

```sh
pip install pypj
```

## Usage

```
$ pypj

┌─┐┬ ┬┌─┐┬
├─┘└┬┘├─┘│    python : 3.8.5
┴   ┴ ┴ └┘    poetry : 1.1.7

Package name: my-package
Do you want to use customized setting? (y/N): N
  Command: poetry new my-package ✨
  Command: poetry config virtualenvs.in-project true ✨
Initialize done 🚀
  Create : .vscode directory ✨
  Create : .vscode/settings.json ✨
  Command: poetry add -D black ✨
  Command: poetry add -D pyproject-flake8 ✨
  Command: poetry add -D mypy ✨
  Command: poetry add -D isort ✨
  Command: poetry add -D pytest ✨
  Command: poetry add -D pytest-cov ✨

Complete! 🚀
Let's make the world better! ✨😋🐍🌎
```

### Requirement

- python
- poetry

## What will be done

- Install elementary dev packages in once
- Configure dev tools on `pyproject.toml`
  - Aggregate all configurations in one

### Details

- Installation
  - Formatter: [`black`](https://github.com/psf/black)
  - Linter: [`pflake8`](https://github.com/csachs/pyproject-flake8)
  - Type linter: [`mypy`](https://github.com/python/mypy)
  - Import formatter: [`isort`](https://github.com/PyCQA/isort)
  - Test framework: [`pytest`](https://github.com/pytest-dev/pytest)
    - Plugin: [`pytest-cov`](https://github.com/pytest-dev/pytest-cov)
- Configuration on `pyproject.toml`
  - Max line length: default is `119`
  - Ignore [`PEP8`](https://pep8.org/): `None`
    - No PEP8 rules are ignored
  - Comfortable `mypy` setting

## Why black and pflake8?

### Formatter: [`black`](https://github.com/psf/black)

`Black` finalize the formats in one. That's the biggest reason it got chosen.

> Black is the uncompromising Python code formatter. By using it, you agree to cede control over minutiae of hand-formatting. In return, Black gives you speed, determinism, and freedom from pycodestyle nagging about formatting. You will save time and mental energy for more important matters.

### Linter: [`pflake8`](https://github.com/csachs/pyproject-flake8)

The configurations must be aggregated in one place, `pyproject.toml`. `pflake8` enables to configure `flake8` on `pyproject.toml`.

## Example of pyproject.toml

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
