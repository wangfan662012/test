# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
import time
import threading


def saysorry():
    print("亲爱的，我错了，我能吃饭了吗？")
    time.sleep(1)


if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=saysorry)
        t.start()  # 启动线程，即让线程开始执行
# 可以明显看出使用了多线程并发的操作，花费时间要短很多
# 当调用start()时，才会真正的创建线程，并且开始执行
