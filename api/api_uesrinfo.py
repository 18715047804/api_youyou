# 修改个人信息  查询
import requests

from api.api_login_session import login

s = requests.Session()

login(s, "杨飞1", "123456")

def update_info(
                name, sex, age, mail):
    url = "http://49.235.92.12:7005/api/v1/userinfo"
    body = {
        "name": name,
        "sex": sex,
        "age": age,
        "mail": mail
    }
    r = s.post(url, json=body)
    return r


if __name__ == '__main__':
    # 自己测试

    r =update_info("杨飞1",sex="M",age=23,mail="100715672@qq.com")
    print(r.json())


