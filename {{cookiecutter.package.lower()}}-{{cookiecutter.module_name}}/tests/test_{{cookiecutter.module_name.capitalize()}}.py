"""Package related tests."""
from {{cookiecutter.module_name.capitalize()}} import __version__


def test_version():
    """Checks correct package version."""
    assert __version__ == "0.1.0"
