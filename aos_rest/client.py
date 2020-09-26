"""
Client for getting documents from https://www.saos.org.pl
"""
import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, Any, Dict

import requests
from requests import Response

AnyDict = Optional[Dict[str, Any]]

LOG = logging.getLogger(__name__)


@dataclass()
class Endpoints:
    """
    SAOS endpoints
    https://www.saos.org.pl/help/index.php/dokumentacja-api/api-pobierania-danych
    https://www.saos.org.pl/help/index.php/dokumentacja-api/api-przeszukiwania-danych
    https://www.saos.org.pl/help/index.php/dokumentacja-api/api-przegladania-danych
    https://www.saos.org.pl/help/index.php/dokumentacja-api/dodatkowe-serwisy
    """
    _auth = 'https://www.saos.org.pl'
    DUMP = '%s/api/dump/judgments' % _auth
    SEARCH = '%s/api/search' % _auth
    DETAIL = '%s/api/' % _auth
    # additional services endpoints
    COURTS = '%s/cc/courts/list' % _auth
    CC_DIVISION = '%s/cc/courts/' % _auth
    SC_CHAMBERS = '%s/sc/chambers/list' % _auth


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

    def __init__(self):
        self._params = {}

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, params: AnyDict):
        if params is not None:
            self._params.update(params)

    @abstractmethod
    def get(self, params: Optional[Dict[str, Any]] = None) -> Response:
        """
        :param params: optional, parameters to be used in API call.
        if not provided, query is using defaults, e.g. first page of results.
        :return: Response object
        """
        pass

    def __repr__(self):
        return str(self._params)


class DumpClient(AbstractClient):
    """
    Client for dumping data from ASOS API.
    """

    def __init__(self):
        super().__init__()
        self._params = {
            "pageSize": 100,
            "pageNumber": 0,
            "withGenerated": True
        }
        LOG.info(self.__repr__())

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

        self.params = params  # update parameters current parameter set

        return requests.get(Endpoints.DUMP, verify=False, params=self.params)


class CommonCourtsClient(AbstractClient):
    """
    Client for fetching data from SAOS common courts services.
    """

    def get(self, params: Optional[Dict[str, Any]] = None) -> Response:
        return requests.get(Endpoints.COURTS, verify=False)


class CourtDivisionClient(AbstractClient):
    """
    Client for fetching data from SAOS court division services.

    Common courts divisions are fetched as per common court ID.
    """

    def get(self, params: Optional[Dict[str, Any]] = None) -> Response:
        try:
            court_id = params.get('CC_COURT_ID')
            url = Endpoints.CC_DIVISION + f'{court_id}/courtDivisions/list'
            return requests.get(url, verify=False)
        except KeyError as _:
            LOG.error('Mandatory parameter CC_COURT_ID not found')

    def get_by_id(self, court_id: int):
        return self.get({'CC_COURT_ID': court_id})


class CourtChambersClient(AbstractClient):
    """
    Client for fetching data from SAOS court chambers service.
    Common Court Chambers are fetched by court ID.
    """

    def get(self, params: Optional[Dict[str, Any]] = None) -> Response:
        pass


class JudgementFormsClient(AbstractClient):
    """
    Client for fetching data from judgement forms SAOS service.
    """

    def get(self, params: Optional[Dict[str, Any]] = None) -> Response:
        pass
