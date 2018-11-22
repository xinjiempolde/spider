import json
f=open('summoner.json','r')
print(json.loads(f.read()))