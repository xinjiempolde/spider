import re
import json
from urllib import request
url='https://pvp.qq.com/web201605/js/item.json'
response=request.urlopen(url)
read=response.read()
read=json.dumps(read)
f=open('sampleLitst.json','w')
f.write(read)
f.close()
