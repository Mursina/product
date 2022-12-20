include .env

# Create virtual environment
venv:
	(\
	rm -rf penv; \
	virtualenv penv -p ${PY_PATH}; \
	source penv/bin/activate; \
	pip install -r requirements.txt; \
	)

# Activate the venv by executing . penv/bin/activate before
run_local:
	python -m product_server