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
from coingecko_openapi_client.api.simple_api import SimpleApi  # noqa: E501
from coingecko_openapi_client.rest import ApiException


class TestSimpleApi(unittest.TestCase):
    """SimpleApi unit test stubs"""

    def setUp(self):
        self.api = coingecko_openapi_client.api.simple_api.SimpleApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_simple_price_get(self):
        """Test case for simple_price_get

        Get the current price of any cryptocurrencies in any other supported currencies that you need.  # noqa: E501
        """
        pass

    def test_simple_supported_vs_currencies_get(self):
        """Test case for simple_supported_vs_currencies_get

        Get list of supported_vs_currencies.  # noqa: E501
        """
        pass

    def test_simple_token_price_id_get(self):
        """Test case for simple_token_price_id_get

        Get current price of tokens (using contract addresses) for a given platform in any other currency that you need.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
