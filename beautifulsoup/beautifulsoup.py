from urllib import request
from bs4 import BeautifulSoup
import pymysql.cursors
# 连接MySQL数据库
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='zxj+15508321787', db='python', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
# 通过cursor创建游标
cursor = connection.cursor()
url="https://pvp.qq.com/web201605/herodetail/510.shtml"
html=request.urlopen(url).read().decode('gbk')
soup=BeautifulSoup(html,features="lxml")
data=soup.find_all(attrs={"class":"skill-desc"})
name=soup.find_all(attrs={"class":"cover-name"})
name=name[0].string
d1=data[0]
d2=data[1]
d3=data[2]
d4=data[3]
d5=data[4]
print(name)
try:
    sql="insert into herodesc values('%s','%s','%s','%s','%s','%s')"%(name,d1,d2,d3,d4,d5)
    cursor.execute(sql)
    connection.commit()
except Exception:
    connection.rollback()
connection.close()