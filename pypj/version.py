from sys import version_info

if version_info.major != 3:
    raise Exception("ERROR: The major version of python is not 3.")

if version_info.minor <= 7:  # <= 3.7 # TODO: make as error when 3.7 is deprecated
    import importlib_metadata as importlib_metadata
else:  # 3.8 <=
    import importlib.metadata as importlib_metadata

try:
    VERSION = importlib_metadata.version(__package__ or __name__)
except Exception:
    raise Exception("ERROR: Failed to load the package version.")
