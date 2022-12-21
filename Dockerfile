FROM python:3.7-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV CSV_DIR=/usr/src/app/product_server/source_files

COPY requirements.txt /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "product_server"]