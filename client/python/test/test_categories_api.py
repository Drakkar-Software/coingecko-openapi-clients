# coding: utf-8

"""
    CoinGecko API V3

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import coingecko_openapi_client
from coingecko_openapi_client.api.categories_api import CategoriesApi  # noqa: E501
from coingecko_openapi_client.rest import ApiException


class TestCategoriesApi(unittest.TestCase):
    """CategoriesApi unit test stubs"""

    def setUp(self):
        self.api = coingecko_openapi_client.api.categories_api.CategoriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_coins_categories_get(self):
        """Test case for coins_categories_get

        List all categories with market data  # noqa: E501
        """
        pass

    def test_coins_categories_list_get(self):
        """Test case for coins_categories_list_get

        List all categories  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
