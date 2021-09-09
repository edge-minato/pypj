import sys
from dataclasses import dataclass
from pathlib import Path

from .cui import ask_no_empty, ask_with_default_num, ask_Yn, ask_yN
from .environment import Version


@dataclass
class PypjSetting(object):
    python_version: Version
    package_name: str = ""
    max_line_length: int = 119
    use_src: bool = False
    venv_in_pj: bool = True
    formatter: str = "black"
    linter: str = "pyproject-flake8"
    type_linter: str = "mypy"
    import_formatter: str = "isort"
    test_fw: str = "pytest"
    tox: str = "tox"
    plugin = ["pytest-cov", "pytest-mock", "tox-gh-actions"]

    def __post_init__(self) -> None:
        self.package_name = ask_no_empty("Package name: ")

    def customize(self) -> None:
        if ask_yN("Do you want to custom setting? (y/N): "):
            self.max_line_length = ask_with_default_num("Max line length (119): ", 119)
            self.use_src = ask_yN("Do you want to use src folder? (y/N): ")
            self.venv_in_pj = ask_Yn("Do you want to keep venv in project? (Y/n): ")
            confirmation = ask_yN("Are you sure? (y/N): ")
            if not confirmation:
                print("Canceled.")
                sys.exit(0)

    def package_name_validate(self) -> None:
        if Path().cwd().joinpath(self.package_name).exists():
            print(f"ERROR: Directory {self.package_name} already exists.")


FLAKE8_SETTING = """
[tool.flake8]
max-line-length = {line_length}
max-complexity = 10
extend-ignore = "E203,"
"""

BLACK_SETTING = """
[tool.black]
line-length = {line_length}
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
"""

MYPY_SETTING = """
[tool.mypy]
# common
python_version = {python_version}
show_column_numbers = true
show_error_context = true
ignore_missing_imports = true
check_untyped_defs = true
disallow_untyped_defs = true
# warning
warn_return_any = true
warn_unused_configs = true
warn_redundant_casts = true
"""

ISORT_SETTING = """
[tool.isort]
profile = "{formatter}"
line_length = {line_length}
"""

TOX_SETTING = """
[tool.tox]
legacy_tox_ini = \"\"\"
[tox]
envlist = PY3X_VERSION, flake8, black, mypy, isort
skipsdist = true
isolated_build = true
skip_missing_interpreters = true
[testenv]
whitelist_externals = poetry
require_locked_deps = true
install_dev_deps = true
commands =
    poetry run pytest ./tests -v --cov=PACKAGE_DIR --cov-branch
[testenv:flake8]
commands = poetry run pflake8 ./PACKAGE_DIR
[testenv:black]
commands = poetry run black ./PACKAGE_DIR
[testenv:mypy]
commands = poetry run mypy ./PACKAGE_DIR
[testenv:isort]
commands = poetry run isort ./PACKAGE_DIR
\"\"\"
"""
