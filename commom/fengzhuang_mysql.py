import pymysql

# 数据库的配置信息

sql_zhanghao = {
    "host": "49.235.92.12",
    "user": "root",
    "password": "123456",
    "database": "apps",
    "port": 3309
}


class DbConnect(object):
     #链接数据库
    def __init__(self, host, user, password, database, port):
        self.mysqllogin= pymysql.Connect(host=host,
                                  user=user,
                                  password=password,
                                  database=database,
                                  port=port,
                                  cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.mysqllogin.cursor() #创建游标激活

    #查询封装
    def select_sql(self, sql):
        """查询sql"""
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    #执行和提交封装v 新增 修改 删除
    def execute_sql(self, sql):
        try:
            self.cursor.execute(sql)
            self.mysqllogin.commit()
        except Exception as msg:
            print("执行sql异常：{}".format(sql))
            print(msg)
            self.mysqllogin.rollback() #回滚数据

    def close(self):
        self.cursor.close()
        self.mysqllogin.close()


# if __name__ == '__main__':
#     # 测试上面的内容
#     mysqllogin = DbConnect(host='49.235.92.12',
#                    user='root',
#                    password='123456',
#                    database='apps',
#                    port=3309)
#     sql1 = 'SELECT * from apiapp_goods WHERE id=73'
#     res1 = mysqllogin.select_sql(sql1)
#     print(res1)
#
#
#     sql2 = 'UPDATE apiapp_goods  SET goodsname="te1st222" WHERE id=73'
#     mysqllogin.execute_sql(sql2)
#
#
#     sql3 = "INSERT INTO `apps`.`apiapp_goods` (`id`, `merchantid`, `goodsname`, `goodsprice`, `stock`, `goodsgroupid`, `goodsstatus`, `price`, `create_time`, `merchantname`, `goodscode`, `update_time`) VALUES ('80', '', 'test222', '49.9', '0', '0', '1', '0', '2021-05-09 23:37:07.205718', '', 'sp_100098', '2021-05-09 23:37:07.205770');"
#     mysqllogin.execute_sql(sql3)
#
#
#     mysqllogin.close()#断开数据库链接


