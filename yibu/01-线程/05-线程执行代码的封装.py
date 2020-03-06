# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang

import threading, time


class MyThred(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            data = "我是线程：{a}  @  {b}".format(a=self.name, b=i)  # name属性中保存的是当前线程的名字
            print(data)


if __name__ == '__main__':
    t = MyThred()
    t.start()
