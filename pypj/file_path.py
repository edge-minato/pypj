from pathlib import Path

from .setting import PypjSetting


class PypjFilePath(object):
    def __init__(self, pwd: Path, setting: PypjSetting) -> None:
        root = pwd.resolve()
        package_name = setting.package_name
        self.root: Path = root  # pwd as absolute path
        self.package_dir = PD = root.joinpath(package_name)  # PD as alias
        self.package_src_dir: Path = PD.joinpath(setting.src_dir)
        self.package_init: Path = self.package_src_dir.joinpath("__init__.py")
        self.package_test: Path = PD.joinpath("tests").joinpath(f"test_{package_name}.py")
        self.pyproject: Path = PD.joinpath("pyproject.toml")
        self.vscode_dir: Path = PD.joinpath(".vscode")
        self.vscode_settings_json: Path = self.vscode_dir.joinpath("settings.json")
        self.makefile: Path = PD.joinpath("Makefile")
        self.readme_md: Path = PD.joinpath("README.md")
        self.readme_rst: Path = PD.joinpath("README.rst")
        self.github_dir: Path = PD.joinpath(".github")
        self.github_workflow_dir: Path = self.github_dir.joinpath("workflows")
        self.wf_unittest: Path = self.github_workflow_dir.joinpath("unittest.yml")
        self.wf_publish: Path = self.github_workflow_dir.joinpath("publish.yml")
        self.dependabot: Path = self.github_dir.joinpath("dependabot.yml")
        self.precommit: Path = PD.joinpath(".pre-commit-config.yaml")

    def print(self) -> None:
        print(vars(self))
