"""Class for scrapping the data using clients."""
from abc import ABC, abstractmethod
from typing import Generator

import urllib3
from requests import Response

from aos_rest.client import AbstractClient

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class AbstractScrapper(ABC):
    """Abstract Scrapper, scrap method used to iteratively get data using
    provided client.

    Instantiated using AbstractClient child object.
    """

    def __init__(self, client: AbstractClient):
        self._client = client

    @abstractmethod
    def get_response_generator(self):
        """Generate response generator using provided client"""


class PageScrapper(AbstractScrapper):
    """Scrapper that is iterating over pages using page id"""

    def __init__(self, client: AbstractClient):
        super().__init__(client)
        self._current_page_number = 0  # by default start at 0

    @property
    def current_page_number(self):
        return self._current_page_number

    @current_page_number.setter
    def current_page_number(self, page_number):
        self._current_page_number = page_number

    def get_response_generator(self) -> Generator[Response, None, None]:
        while True:
            response = self._scrap_by_page()
            self.current_page_number += 1
            if len(response.json()['items']) == 0:
                break
            yield response

    def _scrap_by_page(self) -> Response:
        params = {"pageNumber": self._current_page_number}
        return self._client.get(params)
