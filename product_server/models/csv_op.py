import csv
import json
from product_server.models.product import Product

file = open('/Users/MUr/Downloads/MyProjects/product/product_server/source_files/products.csv')
csv_reader = csv.reader(file)
rows = dict() # CSV data is appended in the dictionsary


class CSV:
    
    def __init__(self): 
        for row in csv_reader:
            rows[csv_reader.line_num] = self.to_dict(Product(csv_reader.line_num, row[0], row[1], row[2], row[3], row[4]))
        
    # Function represents the API of listing the products
    def list_products(self):
        return rows

    def get_product(self, prod_id):
        return rows[prod_id]

    def add_product(self, sku, title, brand, slug, quantity):
        rows[csv_reader.line_num + 1] = Product(csv_reader.line_num + 1, sku, title, brand, slug, quantity)
        csv_writer = csv.writer(file)
        csv_writer.writerow(vars(self.to_dict(rows[csv_reader.line_num + 1])))
        file.close() 

    def to_dict(self,prod):
        prod_dict = vars(prod)
        del prod_dict['product_types']
        del prod_dict['attribute_map']
        return prod_dict