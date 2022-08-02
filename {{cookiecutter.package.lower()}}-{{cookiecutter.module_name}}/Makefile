PROJECT_PATH=${PWD}
SHELL_PROFILE=${SHELL_PROFILE_PATH}

init:
	@echo ""
	@echo "Installing dependencies in poetry environment..."
	@poetry install
	@echo ""
	@echo "Installing pre-commit..."
	@poetry run pre-commit install
	@echo ""
	@echo "Installing kernel..."
	@poetry run python -m ipykernel install --user --name {{cookiecutter.module_name.capitalize()}}
	@echo "{{cookiecutter.module_name.capitalize()}} kernel installed."
	@echo ""
	@echo "Running shell..."
	@poetry shell


pre-commit:
	@cd ${PROJECT_PATH}/
	@git add .
	@pre-commit run

profile:
	@poetry run mprof run ${PROJECT_PATH}/profiling/{{cookiecutter.module_name.lower()}}_profiling.py > ${PROJECT_PATH}/profiling/memory_profiler.log && echo "Se creó el archivo profiling/memory_profiler.log" || echo "Error al correr memory-profiler.";
	@poetry run mprof plot -t "Recorded memory usage" -o ${PROJECT_PATH}/profiling/memory_profiler_plot.png && echo "Se creo la gráfica profiling/memory_profiler_plot.png" || echo "Error al correr memory-profiler."
	@poetry run mprof clean

test:
	@pytest ${PROJECT_PATH}/tests
