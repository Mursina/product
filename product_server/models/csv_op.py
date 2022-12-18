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
        file.close()