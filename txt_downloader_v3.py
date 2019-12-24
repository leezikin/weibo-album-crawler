#coding=utf-8
import re
import os
import time
import subprocess
import sys

def downloadForWindowsByAria2(txt_name):
    exe_path = r'D:\\aria2\\aria2c.exe --all-proxy="localhost:1080" '
    # exe_path_no_proxy = r'D:\\aria2\\aria2c.exe'
    order = exe_path + '-d %s -i %s.txt --save-session=%s_session.txt --conditional-get=true -U="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"'%(txt_name,txt_name,txt_name)
    print(order)
    os.system(order)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        txt_name = sys.argv[1].replace(".txt","")
    else:
        txt_name = input("TXT:")
        txt_name = txt_name+ ""
    isTxtExists = os.path.exists(txt_name + ".txt")
    if isTxtExists:
        mode = 1
        downloadForWindowsByAria2(txt_name)
    else:
        print('该TXT不存在')
