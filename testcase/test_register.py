"""
注册接口测试用例
"""
import pytest
import  allure
from api.api_register import register

#注册之前要删除已存在用户  前置操作
from commom.fengzhuang_mysql import DbConnect,sql_zhanghao  #这里的ql_zhanghao是commom里面的fengzhuang_mysql的账号字典  字典也可以导入

@allure.feature("注册接口模块")
class Test(object):
    @pytest.fixture(scope="function")
    def deleter_register_user(self):
        "删除原先的注册"
        db=DbConnect(**sql_zhanghao)  #**表示把字典里面的参数以键值对的形式传过来   切记
        del_sql = 'DELETE FROM auth_user WHERE username="0000987";'
        db.execute_sql(del_sql)
        # db.close()
        # yield

    @allure.story("注册成功")
    @allure.title("用例标题：账号和密码正确")

    def test_register_success(self,deleter_register_user):  #deleter_register_user  调用删除数据库的函数
        """注册成功"""
        r2 = register(username="0000987",password="222444")
        print(r2.json())
        print("0000987注册成功")
        assert r2.json()["code"] == 0
        assert r2.json()["msg"] == "register success!"


    @allure.story("注册不成功")
    @allure.title("用例标题：同一个号码重复注册")
    def test_register_success2(self):
        """重复注册"""
        r3 = register(username="0000987",password="222444")
        print(r3.json())
        assert r3.json()["code"] == 2000
        assert r3.json()["msg"] == "0000987用户已被注册"
#
# def test_register_zifu_fais():
#     """注册字符不成功"""
#     r = register(username="test111",password="23444",email="123222@qq")
#     print(r.json())
#     assert r.json()["code"] == 3003
#     assert r.json()["msg"] == "参数不合法"
#
#
# def test_register_email_fails():
#     """邮件格式错误"""
#
#     r2 = register(username="5666",password="223444",email="123222@qq")
#     print(r2.json())
#     assert r2.json()["code"] == 3003
#     assert r2.json()["msg"] == "参数不合法"
#
#
# def test_register_null():
#     """注册空职"""
#     r2 = register(username="",password="")
#     print(r2.json())
#     assert r2.json()["code"] == 3003
#     assert r2.json()["msg"] == "参数不合法"
#     assert r2.json()["data"]["username"] == "['该字段不能为空。']"



