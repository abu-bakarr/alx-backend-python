#!/usr/bin/env python3
"""
Unit test for utils.
"""
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Unit test CLass for access_nested_map.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nest_map, path, res):
        """
        Test that the method returns what it is supposed to.
        """
        self.assertEqual(access_nested_map(nest_map, path), res)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nest_map, path, res):
        """
        Test that the method returns what it is supposed to.
        """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nest_map, path)
        self.assertEqual(error.exception.args[0], res)


class TestGetJson(unittest.TestCase):
    """
    test that utils.get_json returns the expected result.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, url, payl, mock):
        """
        Using unittest.mock.patch to patch requests.get.
        It returns a Mock object with a json method
        that returns test_payload.
        """
        mock.return_value = payl
        self.assertEqual(get_json(url), payl)
