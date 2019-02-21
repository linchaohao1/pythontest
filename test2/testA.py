import requests      #调用requests库
funcFlag = '4'    #定义参数username
orderId = 'QY201701121414323212'   #定义参数password
signValue = '311d3af2811978555a3d77493ace0980'
test_url = 'http://115.28.114.32:8015/ms-quyiacct/pa/6110'      #访问登录接口的url地址
datalist = {'funcFlag': funcFlag, 'orderId': orderId,'signValue': signValue}    #将参数添加到需求post的data中
head = {"Content-Type": "application/Json"}   #定义头部
response = requests.post(test_url, json=datalist, headers=head)  #发起一个请求，使用post方法
result = response.text          #读取请求返回的结果
print(result)   #打印返回的结果