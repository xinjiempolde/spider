import urllib
from urllib import request
url='https://pvp.qq.com/web201605/js/summoner.json'
path='/home/xinji/PycharmProjects/spider/'+'summoner.json'
request.urlretrieve(url,path)
