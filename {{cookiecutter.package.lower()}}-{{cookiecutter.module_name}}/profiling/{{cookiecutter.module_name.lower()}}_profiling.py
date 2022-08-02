"""Profiling file."""
from memory_profiler import profile
from profiling.confprofiling import get_source

from {{cookiecutter.module_name.capitalize()}}.model import Model


@get_source(source_path="", source_name="")
@profile
def profiling_{{cookiecutter.module_name.lower()}}_model(source=None):
    """Profiling for model."""
    pass


if __name__ == "__main__":

    profiling_{{cookiecutter.module_name.lower()}}_model()
