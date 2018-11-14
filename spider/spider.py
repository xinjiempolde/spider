from urllib import request
import json
url='http://pvp.qq.com/web201605/js/item.json'
response=request.urlopen(url)
content=response.read()
content=json.loads(content)
print(content)