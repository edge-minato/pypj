# Getting Started with Pypj

## Coding

It's ready to start coding, just proceed with it!

## Git hook

Hit `make update` and `make install` to enable configured pre-commit hooks.

## Versioning

Pypj provides single sourced versioning, which means only `pyproject.toml` contains version information.

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

## CI/CD

GitHub actions workflows are defined.

- `unittest.yml`: Execute unittest for each push, pull request
  - _NOTE_: To integrate with Codecov, uncomment the last part
- `publish.yml`: When a tag on GitHub has been created, this workflow publishes the package to pypi
  - _NOTE_: `PYPI_USERNAME` and `PYPI_PASSWORD` must be configured as GitHub secrets
- `dependabot.yml`: Dependabot will check updates for all dependencies everyday
