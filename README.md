# Product
Simple flask application for a store

## Requirements
Python 3.5.2+

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m product_server
```

and open your browser to here:

```
http://localhost:8080/ui/
```

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t product_server .

# starting up a container
docker run -p 8080:8080 product_server
```