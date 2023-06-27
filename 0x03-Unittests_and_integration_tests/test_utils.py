#!/usr/bin/env python3
"""test_utils module
"""
from parameterized import parameterized
import unittest
from utils import access_nested_map
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
