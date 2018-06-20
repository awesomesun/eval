# coding=utf-8

import os

def show_parameter(dic):

    basedir = os.path.abspath(os.path.dirname(__file__))
    # __file__ refers to the file settings.py
    APP_STATIC_TXT = os.path.join(basedir, 'app/static')
    with open(os.path.join(APP_STATIC_TXT,'parameters.txt'),"w") as f:
    # with open("/home/sunchang/flask/app/static/hello.txt","w") as f:
        for key in dic:
            f.write(key)
            f.write(':' + ' ')
            f.write(dic[key] + '\n')
                # f.write('\t'.join(dic[key][key2]))
                # f.write('\n')


