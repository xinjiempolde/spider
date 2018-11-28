import json
import pymysql.cursors
f=open('herolist.json','r')
f1=f.read()
if f1.startswith(u'\ufeff'):
    f1 = f1.encode('utf8')[3:].decode('utf8')
data=json.loads(f1)
length=len(data)
# 连接MySQL数据库
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='zxj+15508321787', db='python', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)


# 通过cursor创建游标
cursor = connection.cursor()

# 执行数据写入
for i in range(length):
    sql="insert into json values('%d','%s','%s','%d','%d','%s');" %(data[i]['ename'],data[i]['cname'],data[i]['title'],data[i]['new_type'],data[i]['hero_type'],data[i]['skin_name'])
    try:
        cursor.execute(sql)
        connection.commit() #提交到数据库执行，一定要记提交哦
    except Exception:
        connection.rollback() #发生错误时回滚

# 关闭数据连接
connection.close()
f.close()
