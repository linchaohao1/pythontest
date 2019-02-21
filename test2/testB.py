import unittest       #导入unittest
import requests     #导入requests库
import json            #导入json

class LianXi(unittest.TestCase):              #定义一个类，类的首字母要大写哦
       def setUp(self):                                 #初始化
             self.base_url = 'http://115.28.114.32:8015/ms-quyiacct/pa/6110'

       def test_get_success(self):             #定义一个方法，切记要以test开头哦
             datalist = {'funcFlag': '4', 'orderId': 'QY201701121414323212', 'signValue': '311d3af2811978555a3d77493ace0980'}               #定义传参数据
             head = {"Content-Type": "application/Json"}     #定义头部
             r = requests.post(self.base_url, json=datalist, headers=head)          #传入参数
             result = json.loads(r.text)            #使用json格式返回
             print(result)
             self.assertEqual(result['status'], 'FAIL')      #检验返回值

       def test_get_fail(self):
            datalist = {'funcFlag': '4', 'orderId': 'QY201701121414323212',
                        'signValue': '311d3af2811978555a3d77493ace0981'}  # 定义传参数据
            head = {"Content-Type": "application/Json"}  # 定义头部
            r = requests.post(self.base_url, json=datalist, headers=head)  # 传入参数
            result = json.loads(r.text)  # 使用json格式返回
            print(result)
            self.assertEqual(result['status'], 'FAIL')  # 检验返回值


if __name__ == '__main__':
      unittest.main()