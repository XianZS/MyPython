# 1、grep 被查找字符 被搜索文件
```
xzs@ubuntu:~/桌面$ grep c code.txt
c
c#
```
## -v 显示所有不符合的内容
```
xzs@ubuntu:~/桌面$ grep c code.txt -v
python
java
rust
r
```
## -n 显示行号
```
xzs@ubuntu:~/桌面$ grep c code.txt -n
2:c
3:c#
```
## -i 不区分大小写进行查找
```
xzs@ubuntu:~/桌面$ grep c code.txt -i
c
c#
```
# 2、find
