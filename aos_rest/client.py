"""
Client for getting documents from https://www.saos.org.pl
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, Any, Dict

import requests
from requests import Response

Json = Dict[str, Any]


@dataclass()
class Endpoints:
    """
    SAOS endpoints
    """
    _auth = 'https://www.saos.org.pl'
    DUMP = '%s/api/dump/judgments' % _auth
    SEARCH = '%s/api/search' % _auth
    DETAIL = '%s/api/' % _auth
    # todo: add additional services endpoints
    #   https://www.saos.org.pl/help/index.php/dokumentacja-api/dodatkowe-serwisy


class AbstractClient(ABC):
    """
    Abstract REST client for dumping data from:

    For each endpoint, there is a child class with `get` method, that is
    updating or passing additional arguments to query.
    Refer to api documentation for details.

    - dump endpoint: https://www.saos.org.pl/api/dump
    returns full documents.
    - search endpoint: https://www.saos.org.pl/api/search
    returns truncated documents, but can be queried
    - single judgement endpoint: https://www.saos.org.pl/api/judgments/JUDGMENT_ID

    API documentation:
       https://www.saos.org.pl/help/index.php/dokumentacja-api/
    """

    @abstractmethod
    def get(self, params: Optional[Dict[str, Any]] = None) -> Response:
        """
        :param params: optional, parameters to be used in API call.
        if not provided, query is using defaults, e.g. first page of results.
        :return: Response object
        """
        pass


class DumpClient(AbstractClient):
    def get(self, params: Optional[Dict[str, Any]] = None) -> Response:
        """
        Default parameters:
            - pageSize
            - pageNumber
            - withGenerated

        Optional parameters:
            - judgmentStartDate
            - judgmentEndDate
            - sinceModificationDate

        Reference:
            https://www.saos.org.pl/help/index.php/dokumentacja-api/api-pobierania-danych
        """
        default_params = {
            "pageSize": 20,
            "pageNumber": 0,
            "withGenerated": True
        }

        if params is not None:
            default_params.update(params)

        return requests.get(Endpoints.DUMP, verify=False, params=params)


class SearchClient(AbstractClient):
    def get(self, params: Optional[Dict[str, Any]] = None) -> Response:
        pass


if __name__ == '__main__':
    print(Endpoints.DUMP)
