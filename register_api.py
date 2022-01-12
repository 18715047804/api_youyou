# import requests
# import  time
# def register():
#     url = "http://49.235.92.12:7005/api/v1/register"
#
#     username = "张" + str(int(time.time()))
#     body = {
#         "username": username,
#         "password": 123456
#
#     }
#     r = requests.post(url, body)
#     return r
#
# if __name__ == '__main__':
#     a = 1
#
#     while a <= 100:
#         time.sleep(1)
#         r = register()
#
#         print(r.json())
#         print(a)
#
#         a = a + 1
#     print("结束")



