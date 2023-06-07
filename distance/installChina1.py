from subprocess import Popen
comand=['pip', 'install', '-r' "code/yolo5/requirements.txt", '-i' 'https://pypi.tuna.tsinghua.edu.cn/simple']
Popen(comand)