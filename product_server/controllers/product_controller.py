import connexion
import six

from product_server.models.product import Product  # noqa: E501
from product_server import util


def add_product(body):  # noqa: E501
    """Add a new product to the store

    Add a new product to the store # noqa: E501

    :param body: Create a new product in the store
    :type body: dict | bytes

    :rtype: Product
    """
    if connexion.request.is_json:
        body = Product.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_product(id, sku, title, brand, slug, quantity):  # noqa: E501
    """Add a new product to the store

    Add a new product to the store # noqa: E501

    :param id: 
    :type id: int
    :param sku: 
    :type sku: str
    :param title: 
    :type title: str
    :param brand: 
    :type brand: str
    :param slug: 
    :type slug: str
    :param quantity: 
    :type quantity: int

    :rtype: Product
    """
    return 'do some magic!'


def delete_product(product_id, api_key=None):  # noqa: E501
    """Deletes a product

    delete a product # noqa: E501

    :param product_id: Product id to delete
    :type product_id: int
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


def get_product_by_id(product_id):  # noqa: E501
    """Find product by ID

    Returns a single product # noqa: E501

    :param product_id: ID of product to return
    :type product_id: int

    :rtype: Product
    """
    return 'do some magic!'


def list_products(no_of_products=None):  # noqa: E501
    """List the products

    Display the products in the store, by default it lists 10 products # noqa: E501

    :param no_of_products: Specify the number of products to be listed
    :type no_of_products: int

    :rtype: List[Product]
    """
    return 'do some magic!'


def update_product(product_id, sku=None, title=None, brand=None, slug=None, quantity=None):  # noqa: E501
    """Updates a product in the store

     # noqa: E501

    :param product_id: ID of product that needs to be updated
    :type product_id: int
    :param sku: Stock Keeping Unit of product that needs to be updated
    :type sku: str
    :param title: Title of product that needs to be updated
    :type title: str
    :param brand: Brand of product that needs to be updated
    :type brand: str
    :param slug: Slug of product that needs to be updated
    :type slug: str
    :param quantity: Quantity of product that needs to be updated
    :type quantity: int

    :rtype: None
    """
    return 'do some magic!'
