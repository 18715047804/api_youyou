import requests
import  time

#方式1
def register(username,password):
    url = "http://49.235.92.12:7005/api/v1/register"
    body = {
        "username": username,
        "password": password

    }
    r = requests.post(url, body)

    return r

if __name__ == '__main__':
    r = register("杨飞88","123456")
    print(r.json())





#方式2
# def register(username,
#              password
#             ):
#     url = "http://49.235.92.12:7005/api/v1/register"
#     body = {
#         "username": username,
#         "password": password,

#     }
#     r = requests.post(url, body)
#
#     return r
