from subprocess import Popen
comand=['pip', 'install', '-r' "code/yolo5/requirements.txt", '-i' 'http://mirrors.aliyun.com/pypi/simple']
Popen(comand)