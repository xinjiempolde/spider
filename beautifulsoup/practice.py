from urllib import request
from bs4 import BeautifulSoup
response=request.urlopen('http://singheart.cn')
response=response.read().decode('gbk')
fp=open('test.txt','w+')
fp.write(response)
fp.close()