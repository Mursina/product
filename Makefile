# Please create .env file. Example file is provided as example.env
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

# build docker image
build_docker:
	docker build -t product_server .

# Run docker container
run_docker:
	docker run -p 8080:8080 product_server