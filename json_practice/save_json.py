from urllib import request
url='https://pvp.qq.com/web201605/js/herolist.json'
path='/home/xinji/PycharmProjects/json_practice/'+'herolist.json'
request.urlretrieve(url,path)