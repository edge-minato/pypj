from pathlib import Path

from pypj.environment import Version
from pypj.file_path import PypjFilePath
from pypj.setting import PackageName, PypjSetting
from pypj.task.githubactions import GithubActions
from tests.conftest import prepare_dir, validate_yaml


def test_githubactions() -> None:
    # prepare
    PACKAGE = PackageName("test_githubactions")
    package_dir = prepare_dir(PACKAGE)
    # execute
    setting = PypjSetting(Version("0.0.0"), PACKAGE)
    filepath = PypjFilePath(Path().cwd().joinpath("tmp"), setting)
    GithubActions(setting, filepath).execute()
    # assert
    root = package_dir.joinpath(".github")
    workflows = root.joinpath("workflows")
    dependabot = root.joinpath("dependabot.yml")
    unittest = workflows.joinpath("unittest.yml")
    publish = workflows.joinpath("publish.yml")
    assert root.is_dir()
    assert workflows.is_dir()

    assert unittest.exists()
    assert publish.exists()
    assert dependabot.exists()
    assert validate_yaml(dependabot)
    assert validate_yaml(unittest)
    assert validate_yaml(publish)
