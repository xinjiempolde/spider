1.我在linux安装mysql时需要安装libaio，但是在我安装的过程中报错：
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
2.mysql安装教材：https://blog.csdn.net/sweetgirl520/article/details/78131327
