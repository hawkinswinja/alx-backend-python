#!/usr/bin/env python3
"""test module for client"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest import mock


class TestGithubOrgClient(unittest.TestCase):
    """test class for class GithubOrgClient"""
    @parameterized.expand([
        'google',
        'abc'
    ])
    @mock.patch('client.get_json')
    def test_org(self, org, mock_get_json):
        """unit test for org"""
        data = GithubOrgClient(org)
        mock_get_json.return_value = 'Successfull ' + org
        self.assertEqual(data.org, 'Successfull ' + org)
        mock_get_json.assert_called_once_with(data.ORG_URL.format(org=org))
