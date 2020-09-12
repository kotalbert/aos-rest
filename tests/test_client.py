#!/usr/bin/env python

"""Tests for `aos_rest` package."""

import unittest

import dateutil
import urllib3
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

from aos_rest.client import DumpClient

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class TestDumpClient(unittest.TestCase):
    """Tests for `aos_rest.client` package."""

    def test_dump_client_default(self):
        """Check if no error is thrown while getting the default data"""
        dc = DumpClient()
        r = dc.get()
        self.assertTrue(r.ok)

    def test_dump_client_param_update(self):
        dc = DumpClient()
        # test overwrite
        params = {
            "pageSize": 30
        }
        r = dc.get(params)
        self.assertEqual(len(r.json()['items']), 30)

    def test_dump_client_param_start_date(self):
        dc = DumpClient()
        judgement_start_date = '2020-09-01'
        params = {
            "judgmentStartDate": judgement_start_date
        }

        r = dc.get(params)
        jst = dateutil.parser.parse(judgement_start_date)
        for j in r.json()['items']:
            try:
                judgment_date = dateutil.parser.parse(j['judgment_date'])
                self.assertGreater(relativedelta(judgment_date, jst), 0)
            except KeyError:  # most dates are missing or erroneous
                pass

    def test_dump_client_param_end_date(self):
        dc = DumpClient()
        judgement_end_date = '2020-09-01'
        params = {
            "judgmentEndDate": judgement_end_date
        }

        r = dc.get(params)
        jst = dateutil.parser.parse(judgement_end_date)
        for j in r.json()['items']:
            try:
                judgment_date = dateutil.parser.parse(j['judgment_date'])
                self.assertLess(relativedelta(judgment_date, jst), 0)
            except KeyError:  # most dates are missing or erroneous
                pass
