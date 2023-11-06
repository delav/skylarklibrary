import requests


def team2_post01(url, headers, *args, **kwargs):
    """
    发送http update 请求
    :param url:
    :param headers:
    :return:
    """
    print(f"HTTP Post|{url}|{headers}")
    res = requests.post(url, '{}', headers)
    return res
