import requests
from response_codes import Responses


class Probe():
    """
    Abstraction layer for parsing HTML/XML/.JSON to Strings
    """

    def __init__(self) -> None:
        pass

    def parse_URL(self, url : str):

        try:

            response = requests.get(url)

            if response.status_code != 200:

                return Responses.PROBE_ERROR_REQUEST_FAIL, Responses.PAGE_UNREADEABLE
            
            return Responses.PROBE_REQUEST_SUCCESS , response.text
        
        except requests.exceptions.RequestException as e:

            return Responses.PROBE_ERROR_REQUEST_FATAL, Responses.PAGE_UNREACHEABLE
