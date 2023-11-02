from api.deco import keyword
import requests

__version__ = '1.0.0'
ROBOT_LIBRARY_SCOPE = 'GLOBAL'


@keyword
def http_post(url, data, headers):
    print(f"HTTP POST|{url}|{data}|{headers}")
    return {}


@keyword
def http_get(url, headers):
    print(f"HTTP GET|{url}|{headers}")
    return {}
