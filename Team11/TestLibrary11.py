from deco import keyword
import requests


@keyword
def team11_post(url, headers, *args, **kwargs):
    """
    发送http update 请求
    :param url:
    :param headers:
    :return:
    """
    print(f"HTTP PATCH|{url}|{headers}")
    res = requests.post(url, '{}', headers)
    return res
