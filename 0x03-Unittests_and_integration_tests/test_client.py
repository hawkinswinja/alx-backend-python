#!/usr/bin/env python3
"""test module for client"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest import mock

patch = mock.patch


class TestGithubOrgClient(unittest.TestCase):
    """test class for class GithubOrgClient"""
    @parameterized.expand([
        'google',
        'abc'
    ])
    @patch('client.get_json')
    def test_org(self, org, mock_get_json):
        """unit test for org"""
        data = GithubOrgClient(org)
        mock_get_json.return_value = 'Successfull ' + org
        self.assertEqual(data.org, 'Successfull ' + org)
        mock_get_json.assert_called_once_with(data.ORG_URL.format(org=org))

    def test_public_repos_url(self):
        """unit test for method _public_repos_url"""
        with patch.object(GithubOrgClient, 'org',
                          new_callable=mock.PropertyMock) as payload:
            payload.return_value = {'repos_url': 'test data success'}
            a = GithubOrgClient('test')._public_repos_url
            self.assertEqual(a, 'test data success')

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """unit test for public repos"""
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=mock.PropertyMock) as url:
            url.return_value = 'myrepos'
            mock_get_json.return_value = [
                {'name': 'test'},
                {'name': 'test1'},
                {'name': 'test2'}
            ]
            data = GithubOrgClient('test').public_repos()
            mock_get_json.assert_called_once_with('myrepos')
            self.assertEqual(data, ['test', 'test1', 'test2'])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, key, expected):
        """unit test for static has_license"""
        self.assertEqual(GithubOrgClient.has_license(repo, key), expected)
