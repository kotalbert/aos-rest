#!/usr/bin/env python

"""Tests for `aos_rest` package."""

import unittest
import urllib3
from pprint import pprint

from aos_rest.client import DumpClient

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class TestClient(unittest.TestCase):
    """Tests for `aos_rest.client` package."""

    def test_dump_client_default(self):
        """Check if no error is thrown while getting the default data"""
        dc = DumpClient()
        r = dc.get()
        self.assertTrue(r.ok)
