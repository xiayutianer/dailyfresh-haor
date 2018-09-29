# dailyfresh
conda create -n learn2 python=3.6
source activate learn2
source deactivate

#pip包导出
pip freeze > plist.txt

#安装
pip install -r plist.txt

#uwsgi
启动：uwsgi --ini uwsgi.ini
停止：uwsgi --stop uwsgi.pid
重启：uwsgi --reload uwsgi.pid

[uwsgi]
socket=外网ip:端口（使用nginx连接时，使用socket）
http=外网ip:端口（直接做web服务器，使用http）
chdir=项目根目录
wsgi-file=项目中wsgi.py文件的目录，相对于项目根目录
processes=4
threads=2
master=True
pidfile=uwsgi.pid
daemonize=uswgi.log


