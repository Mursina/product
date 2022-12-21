# Product
Simple flask application for a store

## Requirements
Python 3.5.2+

## Usage

Environment sample file has been provided
```
example.env
```

Each operations can be found in the Makefile. We can use make recipe to **setup and run** the project. For example,
```
# Create virtual environment
make venv
```

All APIs can be run using postman collection. The json file can be downloaded in the ropo or can be converted from swagger.yaml file. The path for swagger.yaml,
```
${ROOT_DIR}/product/product_server/swagger/swagger.yaml
```

The main operation is done by following python script

```
csv_op.py
```

To run the server, please execute the following from the root directory or use make recipe:

run the code in the command line
```
python3 -m product_server
```

or run the make recipe
```
make venv
. penv/bin/activate
make run_local
```

and open postman and import postman collection by importing swagger json file


## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t product_server .

# starting up a container
docker run -p 8080:8080 product_server
```

or else simply run the make recipes as below:
```
make run_docker
```

## Functionality

### 1. API functionality

REST API is used for endpoints. The project have following APIs:

1. **List products**:
The number of records of CSV file will be listed as a reponse

2. **Get product**:
Product can be found using product id

3. **Create a new product**:
Add a product which details are passed through the request body. If the product is exist, then inform it inside the response

4. **Delete a product**
Product can be removed from the CSV file using product id. Here **UUID** is used for generating IDs. If the product is not found, 
404 response will be shown

### 2. Request handling
The requests and their responses are formatted as the HTTP format

### 3. Makefile compatibility
We don't need to run each line of code in the command line, we can use make recipe

### 4. Environment file has been set
example.env file is uploaded. User can set it according to their configuration and can change its name as .env 
example.env -> .env

### 5. Docker integration
Project can be run using docker container
