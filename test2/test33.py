import random
import requests
import re

def gettxt(url,book):
    header = [{
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'},
        {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
        {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'},
        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
        {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'}]
    req = requests.get(url,
                       headers=header[random.randint(0, 4)])  # 向目标网站发送 get 请求
    result = req.content
    result = result.decode('gbk')  # 查看网页源代码 看到 charset=gbk，即网页是用的 gbk 编码，故要用 gkb 的编码方式来解码，否则中文就会乱码。
    title_re = re.compile('<h1>(.*?)</h1>')  # 取出文章的标题
    text_re = re.compile('<div id="content" class="showtxt">([\s\S]*?)</div>')  # 由于正文部分有很多的换行符
    title = title_re.findall(result)  # 找出标题
    text = re.findall(text_re, result)  # 找出正文
    title = title[0]  # 由于返回的 title 是列表，故取出列表中的第一项
    text = text[0]
    print(title)  # 打印te
    text = text.split('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;')  # 把字符串按照换行符分割
    text_1 = []  # 添加一个空列表，用来装处理后的正文
    for sentence in text:
        sentence = sentence.strip()  # 去掉每一句两边的空格
        if ' ' in sentence:
            sentence = sentence.replace(' ', '')  # 去掉句子中的
            if '<br/>' in sentence:
                sentence = sentence.replace('<br/>', '')
                text_1.append(sentence)

    t = open(book+'.txt', 'a+')
    t.write(title + '\n')
    for x in text_1:
        t.write(x + '\n')
    t.close()

def geturl(url2):
    header = [{
                  'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'},
              {
                  'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'},
              {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},
              {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'}]
    a = requests.get(url2, headers=header[random.randint(0, 4)])
    b = a.content
    b = b.decode('gbk')
    c_re = re.compile('<dd>(.*?)</dd>')
    c = c_re.findall(b)
    d = []
    for t in c:
        x_re = re.compile('<a href ="(.*?)">')
        x = x_re.findall(t)
        x = x[0]
        d.append('http://www.biqiuge.com' + x)
    del d[0:6]
    return d

def downloadtxt(zongurl,bookname):
    muluurl = geturl(zongurl)
    for q in muluurl:
        gettxt(q,bookname)

def shuchu(txt):
    print(txt)

if __name__ == '__main__':
    a = input("请输入您想下载小说的目录地址：")
    b = input("请输入小说的名字：")
    downloadtxt(a, b)




