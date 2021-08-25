from dataclasses import dataclass


@dataclass
class PypjSetting(object):
    package_name: str
    max_line_length: int = 119
    src_flag: bool = False
    venv_in_pj: bool = True
    formatter: str = "black"
    linter: str = "pyproject-flake8"
    type_linter: str = "mypy"
    import_formatter: str = "isort"
    test_fw: str = "pytest"
    plugin = ["pytest-cov"]


FLAKE8_SETTING = """
[tool.flake8]
max-line-length = {line_length}
max-complexity = 10
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
    | venv
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
