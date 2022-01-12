from api.api_uesrinfo import update_info
import  allure


@allure.feature("更新用户模块")
class Test(object):
    @allure.story("更新成功")
    @allure.title("用例标题：输入正常用户信息")
    def test_update_info_success(self):
        """更新成功用列"""
        print(1) #就是session的s
        r =update_info(name="杨飞1",sex="M",age=223,mail="10071567876@qq.com")
        print(r.json())
        assert  r.json()["code"]==0


    @allure.story("更新失败")
    @allure.title("用例标题：sex字段提故意提填写错误")
    def test_update_info_falsl (self):
        """sex错误"""
        print(1) #就是session的s
        r =update_info(name="杨飞1",sex="1",age=23,mail="10071567676@qq.com")
        print(r.json())
        assert  r.json()["code"]==3333

#
# def test_update_info_fals2 (login_fixture):
#     """name为空"""
#     print(login_fixture) #就是session的s
#     r =update_info(s=login_fixture,name="")
#     print(r.text)
#     assert  r.json()["code"]==4003