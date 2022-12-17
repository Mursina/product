from typing import List
"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""
def check_api_key(api_key, required_scopes):
    return {'test_key': 'test_value'}

def check_productstore_auth(token):
    return {'scopes': ['read:products', 'write:products'], 'uid': 'test_value'}

def validate_scope_productstore_auth(required_scopes, token_scopes):
    return set(required_scopes).issubset(set(token_scopes))


