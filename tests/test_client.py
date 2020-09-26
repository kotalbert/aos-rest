"""Tests for `aos_rest.client` module."""

import unittest

import dateutil
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

from aos_rest.client import *


class DumpClientTestCase(unittest.TestCase):
    """Tests for `aos_rest.client` package."""

    dc = DumpClient()

    def test_dump_client_default(self):
        """Check if no error is thrown while getting the default data"""
        r = self.dc.get()
        self.assertTrue(r.ok)

    def test_dump_client_param_update(self):
        # test overwrite
        params = {
            "pageSize": 30
        }
        r = self.dc.get(params)
        self.assertEqual(len(r.json()['items']), 30)

    def test_dump_client_param_start_date(self):
        judgement_start_date = '2020-09-01'
        params = {
            "judgmentStartDate": judgement_start_date
        }

        r = self.dc.get(params)
        jst = dateutil.parser.parse(judgement_start_date)
        for j in r.json()['items']:
            try:
                judgment_date = dateutil.parser.parse(j['judgment_date'])
                self.assertGreater(relativedelta(judgment_date, jst), 0)
            except KeyError:  # most dates are missing or erroneous
                pass

    def test_dump_client_param_end_date(self):
        judgement_end_date = '2020-09-01'
        params = {
            "judgmentEndDate": judgement_end_date
        }

        r = self.dc.get(params)
        jst = dateutil.parser.parse(judgement_end_date)
        for j in r.json()['items']:
            try:
                judgment_date = dateutil.parser.parse(j['judgment_date'])
                self.assertLess(relativedelta(judgment_date, jst), 0)
            except KeyError:  # most dates are missing or erroneous
                pass


class CommonCourtsTestCase(unittest.TestCase):

    def test_get_common_courts(self):
        client = CommonCourtsClient()
        r = client.get()
        self.assertTrue(r.ok)


class CommonCourtsDivisionsTestCase(unittest.TestCase):

    def test_get_court_divisions_list(self):
        client = CourtDivisionClient()
        r = client.get_by_id(34)
        self.assertTrue(r.ok)
