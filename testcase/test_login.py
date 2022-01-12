import  pytest
import  requests
from  api.api_login_session import login
import  allure

#不用参数化
# def test_login_success():
#     """登录成功"""
#     s =requests.Session()
#     r=login(s,"杨飞1","123456")
#     print(r.json())
#     assert r.json()["code"] == 0
#     assert r.json()["msg"] == "login success!"
#     assert len(r.json()["token"]) == 40





@allure.feature("登录模块")
class Test(object):
#用参数化并且断言赋值
    @allure.story("登录成功和不成功用例")
    @allure.title("{title}")
    @pytest.mark.parametrize("inputuser,inputpsd,expected,title", [
        ["杨飞1","123456", {"code": 0, "msg": "login success!"},"账号密码正确"],
        ["空", "123256",{"code": 3003, "msg": "账号或密码不正确"},"账号为空，密码正确"],
        ["", "",{"code": 3003, "msg": "账号或密码不正确"},"账号和密码都为空"]
    ])
    def test_login_fail(self,inputuser,inputpsd,expected,title):

        allure.dynamic.title("测试标题是：{}".format(title)) #这句话可要可不要

        s =requests.Session()
        r=login(s,user=inputuser,psw=inputpsd)
        print(r.json())

        assert r.json()["code"] == expected["code"]
        assert r.json()["msg"] == expected["msg"]





    #用参数化并且无断言赋值  只针对断言结果全部一样才能用这个
    # @pytest.mark.parametrize("user,psw",[
    #                                      ["杨1飞1","123456"],
    #                                      ["12233","12333"],
    #                                      ["",""],
    #                                      ["","123456"]
    #
    #                                      ])
    #
    # def test_login_fail(user,psw):
    #     """登录失败"""
    #     s =requests.Session()
    #     r=login(s,user,psw)
    #     print(r.json())
    #
    #     assert r.json()["code"] == 3003
    #     assert r.json()["msg"] == "账号或密码不正确"
    #     assert len(r.json()["token"]) == 0





