from pathlib import Path

from pytest_mock import MockFixture

from pypj.file_path import PypjFilePath
from pypj.setting import PackageName, PypjSetting, Version


def path(add: str) -> Path:
    return Path(str(Path().cwd()) + add)


def test_pypj_file_path(mocker: MockFixture) -> None:
    python_version = Version("3.8.0")
    setting = PypjSetting(
        python_version=python_version,
        package_name=PackageName("package"),
        max_line_length=100,
        use_src=False,
        venv_in_pj=False,
    )
    root = Path().cwd()
    fp = PypjFilePath(root, setting)
    assert fp.root == root
    assert fp.package_dir == path("/package")
    assert fp.package_src_dir == path("/package/package")
    assert fp.package_init == path("/package/package/__init__.py")
    assert fp.package_test == path("/package/tests/test_package.py")
    assert fp.pyproject == path("/package/pyproject.toml")
    assert fp.vscode_dir == path("/package/.vscode")
    assert fp.vscode_settings_json == path("/package/.vscode/settings.json")
    assert fp.makefile == path("/package/Makefile")
    assert fp.readme_md == path("/package/README.md")
    assert fp.github_dir == path("/package/.github")
    assert fp.github_workflow_dir == path("/package/.github/workflows")
    assert fp.wf_unittest == path("/package/.github/workflows/unittest.yml")
    assert fp.wf_publish == path("/package/.github/workflows/publish.yml")
    assert fp.dependabot == path("/package/.github/dependabot.yml")
    assert fp.precommit == path("/package/.pre-commit-config.yaml")
    assert len(vars(fp)) == 16  # to check additional fields
