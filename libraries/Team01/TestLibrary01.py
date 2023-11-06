import requests


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
