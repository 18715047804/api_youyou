
import  requests
import yaml
from  api.api_login_session import login
import pytest


#yaml文件读取1
# import os
# from commom.read_yml import readyml
# yaml_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), r"C:\Users\yangfei\Desktop\yoyo_api_preject\data\data.yaml")
# print(yaml_path)
# test_data = readyml(yaml_path)
# print(test_data)



#方式1 yam文件
with open(r"C:\Users\yangfei\Desktop\yoyo_api_preject\data\data.yaml","r",encoding="utf-8") as f:  #打开文件

    #d读取文件内容
    test_data =yaml.safe_load(f)["login2"] #返回一个字段  所以可以用一个变量接受

    print(test_data)


@pytest.mark.parametrize("inputest,expected",test_data)
def test_login_fail(inputest,expected):
    """登录的yaml文件"""
    s =requests.Session()
    r=login(s,**inputest)  #或者  r=login(s,inputuser,inputpsd)
    print(r.json())

    assert r.json()["code"] == expected["code"]
    assert r.json()["msg"] == expected["msg"]










# 方式2
#用参数化并且断言赋值


test_data1 = [
    [{"user": "杨飞1", "psw": "123456"}, {"code": 0, "msg": "login success!"}],
    [{"user": "杨飞2", "psw": "空"}, {"code": 3003, "msg": "账号或密码不正确"}],
    [{"user": "空", "psw": "234333"}, {"code": 3003, "msg": "账号或密码不正确"}],

]
#
#
# @pytest.mark.parametrize("inputest,expected",test_data1)
# def test_login_fail(inputest,expected,):
#     """登录的yaml文件"""
#     s =requests.Session()
#     r=login(s,**inputest)  #或者  r=login(s,inputuser,inputpsd)
#     print(r.json())
#
#     assert r.json()["code"] == expected["code"]
#     assert r.json()["msg"] == expected["msg"]
#
#
#
#
#
#
#
#
#
# #方式3
# #用参数化并且断言赋值
#
# @pytest.mark.parametrize("inputest,expected",[
#     [{"user": "杨飞1", "psw": "123456"}, {"code": 0, "msg": "login success!"}],
#     [{"user": "杨飞2", "psw": "空"}, {"code": 3003, "msg": "账号或密码不正确"}],
#     [{"user": "空", "psw": "234333"}, {"code": 3003, "msg": "账号或密码不正确"}],
#
# ])
# def test_login_fail(inputest,expected,):
#     """登录的yaml文件"""
#     s =requests.Session()
#     r=login(s,**inputest)  #或者  r=login(s,inputuser,inputpsd)
#     print(r.json())
#
#     assert r.json()["code"] == expected["code"]
#     assert r.json()["msg"] == expected["msg"]




