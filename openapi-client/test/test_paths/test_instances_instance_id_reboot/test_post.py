# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import vultr_python_client
from vultr_python_client.paths.instances_instance_id_reboot import post  # noqa: E501
from vultr_python_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestInstancesInstanceIdReboot(ApiTestMixin, unittest.TestCase):
    """
    InstancesInstanceIdReboot unit test stubs
        Reboot Instance  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()
