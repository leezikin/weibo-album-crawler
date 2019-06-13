#coding=utf-8
import re
import os
import time
import subprocess
import sys

def download(url,path):
    isDirExists = os.path.exists(path)
    if not isDirExists:
        os.makedirs(path)
    cmd="wget --user-agent=\"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36\" -t 3 -T 5 -P {0} {1}".format(path,url)
        
    subprocess.call(cmd,shell=True)


def downloadForWindowsByAria2(link, file_name, txt_name):
    exe_path = r'D:\aria2\aria2c.exe'
    order = exe_path + ' -o %s/%s -s5 -x5 %s'%(txt_name, file_name, link)
    order = order.encode('raw_unicode_escape')
    os.system(order)


def isFileExists(fileName,path):
    fileInPath = "%s/%s/%s" %(os.getcwd(),path,fileName)
    if not os.path.exists(fileInPath):
        return False
    else:
        return True


if __name__ == '__main__':
    if len(sys.argv) == 2:
        txt_name = sys.argv[1].replace(".txt","")
    else:
        txt_name = raw_input("TXT:")
    isTxtExists = os.path.exists(txt_name + ".txt")
    if isTxtExists:
        mode = 1
        isDirExists = os.path.exists(txt_name)
        if not isDirExists:
            os.makedirs(txt_name)
        with open('%s.txt'%(txt_name),'r') as f:
           line = f.readline()
           while line:
                file_name = line.split('/')[-1].replace("\n","")
                if file_name != "":
                    if not isFileExists(file_name,txt_name):
                        url_replace = re.sub('(\(|\)|\[|\])',r'\\\1',line)
                        if mode == 1:
                            downloadForWindowsByAria2(url_replace, file_name, txt_name)
                        elif mode ==0:
                            download(url_replace, txt_name)
                    else:
                        print('已存在：' + txt_name + file_name)
                line = f.readline()
    else:
        print('这个TXT不存在啊')