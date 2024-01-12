from deco import keyword
import requests


@keyword
def team1_post01(url, headers, *args, **kwargs):
    """
    发送http update 请求
    :param url:
    :param headers:
    :return:
    """
    print(f"HTTP Post|{url}|{headers}")
    res = requests.post(url, '{}', headers)
    return res
   

@keyword
def team1_post02(url, headers, *args, **kwargs):
    """
    发送http update 请求
    :param url:
    :param headers:
    :return:
    """
    print(f"HTTP Post|{url}|{headers}")
    res = requests.post(url, '{}', headers)
    return res
