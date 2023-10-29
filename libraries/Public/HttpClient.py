import requests


class HttpClient(object):
    __version__ = '1.0.0'
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def http_post(self, url, data, headers):
        print(f"HTTP POST|{url}|{data}|{headers}")
        return {}

    def http_get(self, url, headers):
        print(f"HTTP GET|{url}|{headers}")
        return {}
