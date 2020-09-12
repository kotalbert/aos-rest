"""
Client for getting documents from https://www.saos.org.pl
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, Any, Dict

import requests

Json = Dict[str, Any]


@dataclass()
class Endpoints:
    """
    SAOS endpoints
    """
    _auth = 'https://www.saos.org.pl'
    DUMP = '%s/api/dump/judgements' % _auth
    SEARCH = '%s/api/search' % _auth
    DETAIL = '%s/api/judgments' % _auth
    # todo: add additional services endpoints
    #   https://www.saos.org.pl/help/index.php/dokumentacja-api/dodatkowe-serwisy


class AbstractClient(ABC):
    """
    Abstract REST client for dumping data from:


    - dump endpoint: https://www.saos.org.pl/api/dump
    returns full documents.
    - search endpoint: https://www.saos.org.pl/api/search
    returns truncated documents, but can be querried
    - single judgement endpoint: https://www.saos.org.pl/api/judgments/JUDGMENT_ID

    API documentation:
       https://www.saos.org.pl/help/index.php/dokumentacja-api/
    """

    @abstractmethod
    def get(self, params: Optional[Dict[str, Any]]) -> Json:
        """
        :param params: optional, parameters to be used in API call.
        if not provided, query is using defaults, e.g. first page of results.
        :return:
        """
        pass


class DumpClient(AbstractClient):
    def get(self, params: Optional[Dict[str, Any]]) -> Json:
        r = requests.get(Endpoints.DUMP)
        if r.ok:
            return r.json()
        else:
            r.raise_for_status()


class SearchClient(AbstractClient):
    def get(self, params: Optional[Dict[str, Any]]) -> Json:
        pass


if __name__ == '__main__':
    print(Endpoints.DUMP)
