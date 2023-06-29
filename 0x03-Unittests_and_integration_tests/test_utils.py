#!/usr/bin/env python3
"""test_utils module
"""
import unittest
from unittest import mock
from parameterized import parameterized
from utils import (access_nested_map, get_json, memoize)
from typing import (Sequence, Mapping, Union)


class TestAccessNestedMap(unittest.TestCase):
    """Test class"""
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2),
    ])
    def test_access_nested_map(self, test: Mapping, path: Sequence,
                               expected: Union[Mapping, int]) -> None:
        """Tests the map for the key in path"""
        self.assertEqual(access_nested_map(test, path),  expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, test: Mapping,
                                         path: Sequence) -> None:
        """raise exception error"""
        with self.assertRaises(KeyError):
            access_nested_map(test, path)


class TestGetJson(unittest.TestCase):
    """test module for json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url: str, resp: Mapping) -> None:
        """test the utils.get_json function"""
        with mock.patch('utils.requests.get') as mock_get:
            mock_get.return_value.json.return_value = resp
            self.assertEqual(get_json(url), resp)
            mock_get.assert_called_once()


class TestMemoize(unittest.TestCase):
    """test module for wrapper memoize"""
    def test_memoize(self) -> None:
        """unit test case for memoization"""
        class TestClass:
            def a_method(self) -> int:
                return 42

            @memoize
            def a_property(self) -> int:
                return self.a_method()

        test = TestClass()
        with mock.patch.object(test, 'a_method') as me:
            me.return_value = 30
            a = test.a_property
            b = test.a_property
            self.assertEqual(a, 30)
            self.assertEqual(b, 30)
            me.assert_called_once()
