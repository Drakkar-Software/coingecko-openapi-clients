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
from coingecko_openapi_client.api.derivatives_api import DerivativesApi  # noqa: E501
from coingecko_openapi_client.rest import ApiException


class TestDerivativesApi(unittest.TestCase):
    """DerivativesApi unit test stubs"""

    def setUp(self):
        self.api = coingecko_openapi_client.api.derivatives_api.DerivativesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_derivatives_exchanges_get(self):
        """Test case for derivatives_exchanges_get

        List all derivative exchanges  # noqa: E501
        """
        pass

    def test_derivatives_exchanges_id_get(self):
        """Test case for derivatives_exchanges_id_get

        show derivative exchange data  # noqa: E501
        """
        pass

    def test_derivatives_exchanges_list_get(self):
        """Test case for derivatives_exchanges_list_get

        List all derivative exchanges name and identifier  # noqa: E501
        """
        pass

    def test_derivatives_get(self):
        """Test case for derivatives_get

        List all derivative tickers  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
