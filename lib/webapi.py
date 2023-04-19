import requests
from pprint import  pprint
from hyrobot.common import *

class APIMgr:

    def _printResponse(self,response):
        print('\n\n-------- HTTP response * begin -------')
        print(response.status_code)

        for k,v in response.headers.items():
            print(f'{k}: {v}')

        print('')

        print(response.content.decode('utf8'))
        print('-------- HTTP response * end -------\n\n')

    def mgr_login(self,username='byhy',password='88888888',useProxy=False):
        self.s = requests.Session()

        if useProxy:
            self.s.proxies.update({'http': 'http://127.0.0.1:8888'})

        response = self.s.post("http://127.0.0.1/api/mgr/signin",
                                 data={
                                     'username': username,
                                     'password': password
                                 }
                                 )

        self._printResponse(response)
        return response


    # 客户操作
    def customer_list(self,pagesize=10,pagenumber=1,keywords=''):

        print('列出客户')
        response = self.s.get("http://127.0.0.1/api/mgr/customers",
              params={
                  'action' :'list_customer',
                  'pagesize' :pagesize,
                  'pagenum' :pagenumber,
                  'keywords' :keywords,
              })

        self._printResponse(response)
        return response


    def customer_add(self,name,phonenumber,address):
        print('添加客户')
        response = self.s.post("http://127.0.0.1/api/mgr/customers",
              json={
                    "action":"add_customer",
                    "data":{
                        "name":name,
                        "phonenumber":phonenumber,
                        "address":address
                    }
                })

        self._printResponse(response)
        return response

    def customer_add2(self,data):
        print('添加客户')
        response = self.s.post("http://127.0.0.1/api/mgr/customers",
              json={
                    "action":"add_customer",
                    "data":data
                })

        self._printResponse(response)
        return response

    def customer_del(self,cid):
        print('删除客户')
        response = self.s.delete("http://127.0.0.1/api/mgr/customers",
              json={
                    "action":"del_customer",
                    "id": cid
                })

        self._printResponse(response)
        return response

    def customer_del_all(self):
        response = self.customer_list(100,1)

        theList = response.json()["retlist"]
        for one in theList:
            self.customer_del(one["id"])





    # 药品操作

    def medicine_list(self,pagesize=10,pagenumber=1,keywords=''):
        print('列出药品')
        response = self.s.get("http://127.0.0.1/api/mgr/medicines",
              params={
                  'action' :'list_medicine',
                  'pagesize' :pagesize,
                  'pagenum' :pagenumber,
                  'keywords' :keywords,
              })

        self._printResponse(response)
        return response



    def medicine_del(self,mid):
        print('删除药品')
        response = self.s.delete("http://127.0.0.1/api/mgr/medicines",
              json={
                    "action":"del_medicine",
                    "id": mid
                })

        self._printResponse(response)
        return response


    def medicine_del_all(self):
        response = self.medicine_list(100,1)

        theList = response.json()["retlist"]
        for one in theList:
            self.medicine_del(one["id"])


    # 药品操作


    def order_list(self,pagesize=10,pagenumber=1,keywords=''):
        print('列出订单')
        response = self.s.get("http://127.0.0.1/api/mgr/orders",
              params={
                  'action' :'list_order',
                  'pagesize' :pagesize,
                  'pagenum' :pagenumber,
                  'keywords' :keywords,
              })

        self._printResponse(response)
        return response



    def order_del(self,oid):
        print('删除订单')
        response = self.s.delete("http://127.0.0.1/api/mgr/orders",
              json={
                    "action":"delete_order",
                    "id": oid
                })

        self._printResponse(response)
        return response


    def order_del_all(self):
        response = self.order_list(100,1)

        theList = response.json()["retlist"]
        for one in theList:
            self.order_del(one["id"])

apimgr = APIMgr()

