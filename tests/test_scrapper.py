"""Tests for `aos_rest.client` module."""

import unittest

import aos_rest.scrapper as scrapper
from aos_rest.client import DumpClient


class TestPageIdScrapper(unittest.TestCase):
    dc = DumpClient()
    sc = scrapper.PageScrapper(dc)

    def test_five_first_pages(self):
        for _ in range(5):
            scrap = self.sc.get_response_generator()
            r = next(scrap)
            self.assertTrue(r.ok)
            print(r)

    def test_reaching_end_of_data(self):
        # todo: find why cannot increase page size
        # todo: make stop iteration when items is empty
        self.dc.params = {"pageSize": 100}
        self.sc.current_page_number = 4083
        generator = self.sc.get_response_generator()
        for _ in range(20):
            r = next(generator)
            print(r.content[:250])
