from deco import keyword
import requests

__version__ = '1.0.0'
ROBOT_LIBRARY_SCOPE = 'GLOBAL'


@keyword
def http_post(url, data, headers, **kwargs):
    """
    发送http post请求
    :param url: url
    :param data: data
    :param headers: headers
    :return: response
    """
    print(f"HTTP POST|{url}|{data}|{headers}")
    res = requests.post(url, '{}', headers)
    return res


@keyword
def http_get(url, headers, **kwargs):
    """
    发送http get 请求
    :param url:
    :param headers:
    :return:
    """
    print(f"HTTP GET|{url}|{headers}")
    if not url:
        return None
    res = requests.get(url, headers)
    return res

