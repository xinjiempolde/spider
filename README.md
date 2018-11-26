<br />1.我在linux安装mysql时需要安装libaio，但是在我安装的过程中报错：
错误：GPGME 错误：无数据
错误：GPGME 错误：无数据
错误：GPGME 错误：无数据
错误：GPGME 错误：无数据
错误：数据库 'core' 无效 (无效或已损坏的数据库 (PGP 签名))
错误：数据库 'extra' 无效 (无效或已损坏的数据库 (PGP 签名))
错误：数据库 'community' 无效 (无效或已损坏的数据库 (PGP 签名))
错误：数据库 'multilib' 无效 (无效或已损坏的数据库 (PGP 签名))
下面是我的解决方案：
sudo pacman -Syy
更新一下就好了，就可以sudo pacman -S libaio了
接着初始化时又出现了usr/local/mysql/bin/mysqld: error while loading shared libraries: libnuma.so.1: cannot open shared object file: No such file or directory
解决：sudo pacman -S numctal
<br />2.mysql安装教材：https://blog.csdn.net/sweetgirl520/article/details/78131327
<br/>1.if  _name_=='_main_'代表如果该文件是直接被运行而不是作为模块运行的话，就执行下面的语句。
<br/>2.python类属性既包括数据成员还包括函数元素，通过句点符号来访问。
<br/>3.如何删除本地git账户和密码？vim ~./gitconfig，再把要删除的东西删除掉
<br/>4.git reset HEAD为取消之前的执行的git add
<br/>5.ssh-keygen -t rsa -C “邮箱”ssh-keygen 命令中间没有空格，如果在ssh后面加上空格，会得到Bad escape character ‘ygen’.的错误。
<br/>6.如何配置github ssh key：https://www.jianshu.com/p/861f1ce33f6a
<br/>7.如何保存列表或字典：https://blog.csdn.net/guoweish/article/details/47106263
<br/>8.json.dumps是将字典转换为字符串，而json.loads是将字符串转换为字典。
<br/>9.个人认为python Flask快速入门的一个教程：https://blog.csdn.net/liuchunming033/article/details/45536211
<br/>10.装饰器入门的一篇我能理解的文章：https://foofish.net/python-decorator.html
<br/>11.mariadb启动：systemctl start mariadb.service
<br/>12.注意：在数据库中建立数据库表的时候别把’);‘放在单独放在最后一行，否则会出错;
<br/>13.我能看懂的mysql入门教程（mariadb）:http://blog.51cto.com/xpleaf/1712821;
<br/>14.NOTE : 这里的dump()方法和load方法()没有s，如果处理的是字符串而不是文件，就需要➕加上s;
<br/>15.json.loads(open('herolist.json','r').read())时，herolist有BOM头需要处理，否则会出错。

