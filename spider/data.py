import re
from urllib import request
response=request.urlopen("http://www.baidu.com")
html=response.read()
html=html.decode('utf-8')
reg=r'(?<=<title>).+?(?=</title>)'
regcp=re.compile(reg)
content=re.search(regcp,html)
print(content.group(0))