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
from coingecko_openapi_client.api.companies__beta_api import CompaniesBetaApi  # noqa: E501
from coingecko_openapi_client.rest import ApiException


class TestCompaniesBetaApi(unittest.TestCase):
    """CompaniesBetaApi unit test stubs"""

    def setUp(self):
        self.api = coingecko_openapi_client.api.companies__beta_api.CompaniesBetaApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_companies_public_treasury_coin_id_get(self):
        """Test case for companies_public_treasury_coin_id_get

        Get public companies data  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()