#coding=utf-8
from selenium import webdriver
import selenium.common.exceptions
import os
import time

def login():
    browser.get("https://weibo.com/")
    login = 0
    while login != 1:
        login = input("完成登录后输入'1':")


def user_select_process(mode):
    if mode == 1:
        filename = raw_input("归档文件名:")
        album_process(filename)
        return 1


def album_process(filename):
    lastestLastLine = 0
    while 1 == 1:
        hello = browser.find_elements_by_css_selector("ul.photoList.clearfix > li > a > img")
        if lastestLastLine == 0 and os.path.exists(filename):
            lastLine = get_last_line(filename)
            lastestLastLine = 1
            if lastLine != None:
                lastLine = lastLine.split("\r\n")[0]
        elif lastestLastLine == 0:
            lastLine = None
            lastestLastLine = 1
            open(filename,'w').close()

        if hello:
            listLastSrc = hello[-1].get_attribute('src').encode('raw_unicode_escape')
        if hello and listLastSrc != lastLine:
            writeFile = open(filename,'a+')
            for i in range(len(hello)):
                writeFile.write(hello[i].get_attribute('src') + '\n')
            lastestLastLine = 0
            print('Done,last line:' + hello[-1].get_attribute('src'))
            writeFile.close()
            currentFinnish = 1
        elif hello and currentFinnish == 1:
            try:
                nextPage = browser.find_element_by_css_selector("a.M_btn_c.next")
                nextPage.click()
                currentFinnish == 0
            except selenium.common.exceptions.NoSuchElementException:
                print("找不到下一页")
                break
        time.sleep(0.75)
    finishing_process()


def finishing_process():
    continueKey = input("是否继续工程(0,1):")
    if continueKey == 1:
        print("请手动跳转至获取页面")
        user_select_process(1)
    elif continueKey == 0:
        exit()
    else:
        finishing_process()


def get_last_line(filename):
        filesize = os.path.getsize(filename)
        if filesize == 0:
            return None
        else:
            with open(filename, 'rb') as fp:
                offset = -8
                while -offset < filesize:
                    fp.seek(offset, 2)
                    lines = fp.readlines()
                    if len(lines) >= 2:
                        return lines[-1]
                    else:
                        offset *= 2
                fp.seek(0)
                lines = fp.readlines()
                return lines[-1]


if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.maximize_window()
    login()
    print("请手动跳转至获取页面")
    user_select_process(1)