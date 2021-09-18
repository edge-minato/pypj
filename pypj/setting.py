from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import List

from .cui import ask_with_default_num, ask_Yn, ask_yN
from .environment import Version
from .exception import Emsg, PypjError
from .type_def import Formatter, ImportSorter, Linter, Plugin, TestFramework, TypeChecker


class PackageName(str):
    @staticmethod
    def is_valid(name: str) -> bool:
        regex = r"^[a-zA-Z][0-9a-zA-Z\-_]*"
        return bool(re.fullmatch(regex, name))

    @staticmethod
    def strict_format(package_name: str) -> str:
        return package_name.replace("-", "_").lower()

    def __new__(cls, name: str) -> PackageName:
        if not PackageName.is_valid(name):
            raise PypjError(Emsg.INVALID_PACKAGE_NAME)
        self = super().__new__(cls, PackageName.strict_format(name))
        return self


@dataclass
class PypjSetting(object):
    python_version: Version
    package_name: PackageName
    max_line_length: int = 119
    # use or not
    use_src: bool = False
    venv_in_pj: bool = True
    guthub_actions: bool = True
    vscode: bool = True
    makefile: bool = True
    precommit: bool = True
    # software
    formatter: Formatter = Formatter.BLACK
    linter: Linter = Linter.PFLAKE8
    type_checker: TypeChecker = TypeChecker.MYPY
    import_sorter: ImportSorter = ImportSorter.ISORT
    unittest_framework: TestFramework = TestFramework.PYTEST
    test_framework: TestFramework = TestFramework.TOX
    plugin: List[Plugin] = field(
        default_factory=lambda: [
            Plugin.FLAKE8_BUGBEAR,
            Plugin.PYTEST_COV,
            Plugin.PYTEST_MOCK,
            Plugin.TOX_GH_ACTIONS,
        ]
    )

    def __post_init__(self) -> None:
        self.validate_package_dir()
        self.src_dir: str = self.package_name  # as default

    def customize(self) -> None:
        self.max_line_length = ask_with_default_num("Max line length (119): ", 119)
        self.use_src = ask_yN("Use src directory")
        self.src_dir = "src" if self.use_src else self.package_name
        self.venv_in_pj = ask_Yn("Keep venv in project")
        self.guthub_actions = ask_Yn("Use github workflows")
        self.vscode = ask_Yn("Use vscode settings")
        self.precommit = ask_Yn("Use pre-commit")
        self.makefile = ask_Yn("Use command alias as Makefile")

    def validate_package_dir(self) -> None:
        if Path().cwd().joinpath(str(self.package_name)).exists():
            print(f"ERROR: Directory {self.package_name} already exists.")
            sys.exit(1)


FLAKE8_SETTING = """
[tool.flake8]
max-line-length = {line_length}
max-complexity = 10
select = "C,E,F,W,B"
ignore = "E203"
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
    poetry install -vv --no-root
    pytest ./tests -v --cov=PACKAGE_DIR --cov-branch --durations=0
[testenv:flake8]
commands = poetry run pflake8 --statistics ./PACKAGE_DIR ./tests
[testenv:black]
commands = poetry run black ./PACKAGE_DIR ./tests
[testenv:mypy]
commands = poetry run mypy ./PACKAGE_DIR ./tests
[testenv:isort]
commands = poetry run isort ./PACKAGE_DIR ./tests
\"\"\"
"""
