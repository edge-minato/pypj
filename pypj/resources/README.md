# Getting Started with Pypj

##

## Versioning

Pypj provides single sourced versioning.
Only `pyproject.toml` contains version information.

## Alias

Some aliases are defined.

- `make install`: Install dependencies
- `make test`: Execute unittest
- `make clean`: Remove built stuff
- `make build`: Build your package
- `make run`: Run your command

## CI/CD

GitHub actions workflows are defined.

- `unittest.yml`: Execute unittest for each push, pull request
  - _NOTE_: To integrate Codecov, uncomment the last part
