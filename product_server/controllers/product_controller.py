import connexion
import six

from product_server.models.product import Product  # noqa: E501
from product_server import util

from product_server.models.csv_op import CSV

csv_obj = CSV()

def add_product(body):  # noqa: E501
    """Add a new product to the store

    Add a new product to the store # noqa: E501

    :param body: Create a new product in the store
    :type body: dict | bytes

    :rtype: Product
    """
    if connexion.request.is_json:
        body = Product.from_dict(connexion.request.get_json())  # noqa: E501
    return csv_obj.add_product(body.sku, body.brand, body.slug, body.title, body.quantity)


def delete_product(product_id, api_key=None):  # noqa: E501
    """Deletes a product

    delete a product # noqa: E501

    :param product_id: Product id to delete
    :type product_id: int
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return csv_obj.delete_product(product_id)


def get_product_by_id(product_id):  # noqa: E501
    """Find product by ID

    Returns a single product # noqa: E501

    :param product_id: ID of product to return
    :type product_id: int

    :rtype: Product
    """
    return csv_obj.get_product(product_id)


def list_products(no_of_products=None, brand_name=None, skip=None, limit=None):  # noqa: E501
    """List the products

    Display the products in the store, by default it lists 10 products # noqa: E501

    :param no_of_products: Specify the number of products to be listed
    :type no_of_products: int

    :rtype: List[Product]
    """
    return csv_obj.list_products(no_of_products, brand_name, skip, limit)
