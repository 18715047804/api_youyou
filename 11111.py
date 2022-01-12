import requests

from api.api_login_session import login
s = requests.session()
login(s,"杨飞1", "123456")

def add_address(tel,name,address,postal):
    url = "http://49.235.92.12:7005/api/v2/address"
    body = {
        "tel": tel,
        "name": name,
        "address": address,
        "postal": postal
    }
    r = s.post(url, json=body)
    return r
#
# if __name__ == '__main__':
#
#     r = add_address(tel="18787877777",name="22",address="北京1",postal="12322")
#     #或者r = add_address("13433444344","杨飞11","北京1",12322")
#     print(r.json())








# def add_address(tel="15220000333",
#                 name="悠悠",
#                 address="上海市", postal="10086"):
#     url = "http://49.235.92.12:7005/api/v2/address"
#     body = {
#         "tel": tel,
#         "name": name,
#         "address": address,
#         "postal": postal
#     }
#     r = s.post(url, json=body)
#     return r
#
# if __name__ == '__main__':
#
#     r = add_address(tel="13433444344",name="杨飞11",address="北京1",postal="12322")
#     print(r.json())