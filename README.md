# 以web 服务的形式进行数据传输
在运行程序的时候，需要获得腾讯词向量，但是每次加载需要的时间太久了，以 web 服务的形式进行词向量的获取

### 运行服务器进程
`python3 server.py`
### 运行客户端进程
`python3 client.py`

查看某端口占用情况
lsof -i :端口号
非root用户执行
kill -9 $(sudo lsof -i tcp:进程号 -t)