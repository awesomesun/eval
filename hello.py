# coding=utf-8

import os
basedir = os.path.abspath(os.path.dirname(__file__))


# __file__ refers to the file settings.py
APP_STATIC_TXT = os.path.join(basedir, 'app/static')
with open(os.path.join(APP_STATIC_TXT,'hello.txt'),"w") as f:
# with open("/home/sunchang/flask/app/static/hello.txt","w") as f:
        f.write("It is a 测试啊!")


