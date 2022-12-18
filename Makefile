# Create virtual environment
# Activate the venv by executing . penv/bin/activate
venv:
	(\
	rm -rf penv; \
	virtualenv penv -p ${PY_PATH}; \
	source penv/bin/activate; \
	pip install -r requirements.txt; \
	)

run_local:
	python -m product_server