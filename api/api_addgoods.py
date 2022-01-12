import  requests


from api.api_login_session import login

s =requests.Session()
r =login(s,"杨飞1","123456")  #只关注账号密码就行了
print(r.json())


def addgoods(goodsname:str="24243433",cod:str="sp_132424"):
    url1= "http://49.235.92.12:7005/api/v2/goods"

    # cod="sp_"+str(int(time.time()))

    bady1 ={
         "goodsname": goodsname,
         "goodscode": cod
             }

    # h={
    # 'Authorization': 'Token %s'%(token_vleu)   #或者 'Authorization': 'Token {}'.format(token_vleu)    #不要了  sisson会话里面自动保存了
    #   }

    r =s.post(url1,json =bady1)
    return r

if __name__ == '__main__':
    r =addgoods()
    print(r.json())



#方法2
# def addgoods(goodsname, cod):
#     url1 = "http://49.235.92.12:7005/api/v2/goods"
#
#     # cod="sp_"+str(int(time.time()))
#
#     bady1 = {
#         "goodsname": goodsname,
#         "goodscode": cod
#     }
#
#     # h={
#     # 'Authorization': 'Token %s'%(token_vleu)   #或者 'Authorization': 'Token {}'.format(token_vleu)    #不要了  sisson会话里面自动保存了
#     #   }
#
#     r = s.post(url1, json=bady1)
#     return r




