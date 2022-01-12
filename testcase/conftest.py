import  pytest
import requests

from api.api_login_session import login


@pytest.fixture(scope="session")
def login_fixture():
    """前置登录"""
    print("看是不是登录一次")
    s=requests.Session()
    login(s,"杨飞1","123456")
    # return  s  #s对象 里面已经存token了
    yield s  #比retunr强大  可以执行后面操作    迭代器
    print("后置操作 数据清理")
    s.close()