# Getting Started with pypj

First of all, what should be done is creating and updating a venv. If the directory is not initialized with `git`, `make install` may fail because it fails to install `pre-commit` hooks.

```sh
# git init # if it is not done
make install
make update
# try test
make test
```

NOTE: This kick starter guide suppose the default settings of `pypj`. If you customized some configurations and disabled the features or tools, that could be difference with this guide.

## Coding

It's ready to start coding, just proceed with it!

## Git hook

See the `.pre-commit-config.yaml` to know what is configured.
Hit `make update` and `make install` to enable configured pre-commit hooks.

## Versioning

Single sourced versioning is provided, which means only `pyproject.toml` contains version information.

## Alias

Some aliases are defined.

- `make install`
  - Install dependencies
  - Install pre-commit hooks
- `make update`
  - Update dependencies
  - Update pre-commit hooks
- `make clean`: Remove built stuff
- `make build`: Build your package
- `make run`: Run your command
- `make debug`: Run unittest with showing stdout
- `make test`: Execute unittest
- `make style`: Run code styling tools


## Test

Tests get triggered by a little bit complicated flow as following. If `tox` is not required, of course `poetry run pytest ./tests` works fine.

```md
# env: command

system      : make test
system      : poetry run tox
poetry.venv : tox
tox.venv    : poetry install (*1)
tox.venv    : pytest ./tests
-> Test runs on each venv of tox

(*1): "poetry" command at system is called at venv of tox because of configuration "whitelist_externals = poetry"
```

## CI/CD

GitHub actions workflows are defined.

- `unittest.yml`: Execute unittest for each push, pull request
  - _NOTE_: To integrate with Codecov, uncomment the last part
- `publish.yml`: When a tag on GitHub has been created, this workflow publishes the package to pypi
  - _NOTE_: `PYPI_USERNAME` and `PYPI_PASSWORD` must be configured as GitHub secrets
- `dependabot.yml`: Dependabot will check updates for all dependencies everyday
