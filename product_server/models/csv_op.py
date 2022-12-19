import csv
import json
from product_server.models.product import Product

file = open('/Users/MUr/Downloads/MyProjects/product/product_server/source_files/products.csv')
csv_reader = csv.reader(file)
rows = dict() # CSV data is appended in the dictionsary


class CSV:
    
    def __init__(self): 
        for row in csv_reader:
            prod = Product(csv_reader.line_num, row[0], row[1], row[2], row[3], row[4])
            rows[csv_reader.line_num] = vars(prod)
        
    # Function represents the API of listing the products
    def list_products(self):
        return rows

    def get_product(self, prod_id):
        return rows[prod_id]

    def add_product(self, sku, title, brand, slug, quantity):
        rows[csv_reader.line_num + 1] = Product(csv_reader.line_num + 1, sku, title, brand, slug, quantity)
        csv_writer = csv.writer(file)
        csv_writer.writerow(rows[csv_reader.line_num + 1])
        file.close()  