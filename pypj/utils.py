from functools import reduce
from pathlib import Path
from typing import List, Tuple

from pypj.const import INDENT, Emoji
from pypj.resource import get_my_resource
from pypj.type_def import ReplaceWords


def setValue(wordsList: List[Tuple[str, str]], string: str) -> str:
    return reduce(lambda s, kv: s.replace(*kv), wordsList, string)


def writeResource(file: Path, replace_words: ReplaceWords, prefix: str = "") -> None:
    with file.open(mode="w") as f:
        f.write(setValue(replace_words, get_my_resource(file.name)))
    print(f"{INDENT}Create : {prefix}{file.name} {Emoji.OK}")
