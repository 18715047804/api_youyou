import  pytest
import time
import  allure
from api.api_addgoods import addgoods


@allure.feature("添加商品模块")
class Testaddgoods(object):

    @allure.story("添加商品成功")
    @allure.title("用例标题：运用时间戳添加")
    def test_addgoods(self):
        """添加商品无限次成功"""
        cod="sp_"+str(int(time.time()))
        r=addgoods("12444",cod)
        print(r.json())
        assert r.json()["code"] == 0
        assert r.json()["msg"] == "success!"


    @allure.story("添加商品失败")
    @allure.title("用例标题：商品名称错误，参数不合法")
    def test_addgoods_fasl(self):
        """测试商品名称"""
        r=addgoods("12444","sp14536")
        print(r.json())
        assert r.json()["code"] == 3003
        assert r.json()["msg"] == "参数不合法"



    @allure.story("添加商品失败")
    @allure.title("用例标题：商品名称为空")
    def test_addgoods_fas2(self):
        """测试商品名称不填"""
        r=addgoods("12444","")
        print(r.json())
        assert r.json()["code"] == 2000
        assert r.json()["msg"] == "缺少必填项goodscode"

