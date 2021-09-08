from pathlib import Path

from .setting import PypjSetting


class PypjFilePath(object):
    def __init__(self, pwd: Path, setting: PypjSetting) -> None:
        root = pwd.resolve()
        self.root: Path = root  # as absolute path
        self.package_dir: Path = root.joinpath(setting.package_name)
        src_dir = "src" if setting.use_src else setting.package_name
        self.package_src_dir: Path = self.package_dir.joinpath(src_dir)
        self.package_init: Path = self.package_src_dir.joinpath("__init__.py")
        self.pyproject: Path = self.package_dir.joinpath("pyproject.toml")
        self.vscode_dir: Path = self.package_dir.joinpath(".vscode")
        self.vscode_settings_json: Path = self.vscode_dir.joinpath("settings.json")
        self.makefile: Path = self.package_dir.joinpath("Makefile")
        self.readme_md: Path = self.package_dir.joinpath("README.md")
        self.readme_rst: Path = self.package_dir.joinpath("README.rst")
        self.github_dir: Path = self.package_dir.joinpath(".github")
        self.github_workflow_dir: Path = self.github_dir.joinpath("workflows")
        self.wf_unittest: Path = self.github_workflow_dir.joinpath("unittest.yml")
        self.wf_publish: Path = self.github_workflow_dir.joinpath("publish.yml")
        self.dependabot: Path = self.github_dir.joinpath("dependabot.yml")

    def print(self) -> None:
        print(vars(self))
