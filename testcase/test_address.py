import  pytest
import  allure
from api.api_address import add_address

#存在参数化的allur报告标题   title

@allure.feature("地址接口模块")
class Test(object):
    @pytest.mark.parametrize("tel,name,address,postal,title",
                             [
                                         ["18987878766","yang1","合肥","2344","测试号码，姓名，地址"],
                                         ["188787765677", "yang2", "合肥1", "244","测试号码，姓名，地址"],
                                         ["","","","","测试不填写任何一条数据"],
                                         ["1099899", "yang3", "合肥2", "222344","测试手机号码错误，其他数据正常"],



                                         ]
                             )


    @allure.story("添加地址成功和失败用例参数化")
    @allure.title("{title}")
    def test_address(self,tel,name,address,postal,title):
        """添加成功地址"""

        allure.dynamic.title("动态测试标题：{}".format(title)) #也可以不用这一句  直接用上面的title也行的

        r=add_address(tel,name,address,postal)
        print(r.json())
        assert r.json()["code"] == 0
        assert r.json()["msg"] == "success!"