from urllib import request
import json
import os
response=request.urlopen("https://pvp.qq.com/web201605/js/herolist.json")
hero_json=json.loads(response.read())
hero_num=len(hero_json)
hero_name=hero_json[0]['cname']
skin_names=hero_json[0]['skin_name'].split('|')
for i in range(hero_num):
    skin_names=hero_json[i]['skin_name'].split('|')
    for cnt in range(len(skin_names)):
        save_file_name='/home/xinji/PycharmProjects/spider/images/'+str(hero_json[i]['ename'])+'.jpg'
        skin_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(hero_json[i]['ename']) + '/' + str(hero_json[i]['ename']) + '-bigskin-' + str(cnt + 1) + '.jpg'
        request.urlretrieve(skin_url,save_file_name)