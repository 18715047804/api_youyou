import  requests

#夸请求保持参数

# s =requests.Session()   #先不用  调用的时候用


#第一步  运行登录
def login(s:requests.Session,user:str="杨飞1",psw:str="123456"):   #s  先定义一个形参 后面传实参  requests.Session()
    url = "http://49.235.92.12:7005/api/v1/login"
    body = {
        "username": user,
        "password": psw
    }
    r = s.post(url, json=body)

    token=r.json()["token"]

#更新token到头部
    h = {
        "Authorization": "Token {}".format(token)
    }



#第三步合并字典  更新请求头部

    s.headers.update(h)
    return r  #返回对象  存在token了



if __name__ == '__main__':
    s =requests.Session()
    r =login(s,"杨飞1","123456")
    print(r.json())
    print(s.headers)
#     #{'User-Agent': 'python-requests/2.26.0', 'Accept-Encoding': 'gzip, deflate, br', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'Token e574f7acd24438293b5823ceee302169b585b665'}