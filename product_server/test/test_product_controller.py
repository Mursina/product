# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from product_server.models.product import Product  # noqa: E501
from product_server.test import BaseTestCase


class TestProductController(BaseTestCase):
    """ProductController integration test stubs"""

    def test_add_product(self):
        """Test case for add_product

        Add a new product to the store
        """
        body = Product()
        data = dict(id=789,
                    sku='sku_example',
                    title='title_example',
                    brand='brand_example',
                    slug='slug_example',
                    quantity=789)
        response = self.client.open(
            '/product',
            method='POST',
            data=json.dumps(body),
            data=data,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_product(self):
        """Test case for delete_product

        Deletes a product
        """
        headers = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/product/{productId}'.format(product_id=789),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_product_by_id(self):
        """Test case for get_product_by_id

        Find product by ID
        """
        response = self.client.open(
            '/product/{productId}'.format(product_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_products(self):
        """Test case for list_products

        List the products
        """
        query_string = [('no_of_products', 789)]
        response = self.client.open(
            '/products',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_product(self):
        """Test case for update_product

        Updates a product in the store
        """
        query_string = [('sku', 'sku_example'),
                        ('title', 'title_example'),
                        ('brand', 'brand_example'),
                        ('slug', 'slug_example'),
                        ('quantity', 789)]
        response = self.client.open(
            '/product/{productId}'.format(product_id=789),
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
