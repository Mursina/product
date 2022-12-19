import csv
from product_server.models.product import Product
import os

rows = dict() # CSV data is appended in the dictionsary


class CSV:

    def __init__(self): 
        pass
        
    # Function represents the API of listing the products
    def list_products(self):
        with open('/Users/MUr/Downloads/MyProjects/product/product_server/source_files/products.csv') as self.file:
            self.csv_reader = csv.reader(self.file)
            for row in self.csv_reader:
                rows[self.csv_reader.line_num] = self.to_dict(Product(self.csv_reader.line_num, row[0], row[1], row[2], row[3], row[4]))
            return {
                "description": "Successful operation",
                "status": 200,
                "response": rows
            } 

    # Function represents the API of getting the product by product_id
    def get_product(self, prod_id):
        try:
            return rows[prod_id]
        except:
            return {
                "description": "Product is not found",
                "status": 404,
                "title": "Internal Server Error",
                "type": "about:blank"
            }
        

    # Function represents the API of adding the product
    def add_product(self, sku, title, brand, slug, quantity):

        with open('/Users/MUr/Downloads/MyProjects/product/product_server/source_files/products.csv','a') as f_append:
            p = Product(len(rows)+ 1, sku, title, brand, slug, quantity)
            rows[len(rows)+ 1] = self.to_dict(p)
            current_row = list(rows[len(rows)].values())

            # Remove the id before append the record in the CSV file
            current_row.pop(0)

            # Append the list in the last line of CSV file
            csv_writer = csv.writer(f_append)
            csv_writer.writerow(current_row)
            
            return {
                "description": "Successful operation",
                "status": 200,
                "response": self.to_dict(p)
            } 

    # Function represents the API of deleting the product by product_id
    def delete_product(self, product_id):

        rows = self.list_products()
        with open('/Users/MUr/Downloads/MyProjects/product/product_server/source_files/products.csv') as self.file, open('/Users/MUr/Downloads/MyProjects/product/product_server/source_files/output.csv', 'w') as output:
            self.csv_reader = csv.reader(self.file)

            _sku = rows[product_id]['sku'] # Find relevant sku
            rows.pop(product_id, None)
            for row in self.csv_reader:
                if row[0] != _sku:
                    csv_writer = csv.writer(output)
                    csv_writer.writerow(row)
        os.remove('/Users/MUr/Downloads/MyProjects/product/product_server/source_files/products.csv')
        os.rename(r'/Users/MUr/Downloads/MyProjects/product/product_server/source_files/output.csv', r'/Users/MUr/Downloads/MyProjects/product/product_server/source_files/products.csv')

    # Function represents the API of converting the Product model into dictionary
    def to_dict(self,prod):
        prod_dict = vars(prod)
        prod_dict.pop('product_types', None)
        prod_dict.pop('attribute_map', None)
        return prod_dict