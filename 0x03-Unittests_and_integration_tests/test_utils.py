#!/usr/bin/env python3
"""test_utils module
"""
from parameterized import parameterized
import unittest
from utils import access_nested_map, Mapping, Sequence


class TestAccessNestedMap(unittest.TestCase):
    """Test class"""
    @parameterized.expand([({'a': 1}, ('a',)),
                          ({'a': {'b': 2}}, ('a',)),
                          ({'a': {'b': 2}}, ('a', 'b'))])
    def test_access_nested_map(self, test: Mapping, path: Sequence) -> None:
        """Tests the map for the key in path"""
        self.assertEqual(access_nested_map(test, path),  get_val(test, path))

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, test: Mapping,
                                         path: Sequence) -> None:
        """raise exception error"""
        self.assertRaises(KeyError, access_nested_map(test, path))


def get_val(data: Mapping, path: Sequence) -> any:
    """get value from data using key"""
    for key in path:
        data = data[key]
    return data
