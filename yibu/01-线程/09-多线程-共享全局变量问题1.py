# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
import threading
import time

g_num = 0


def work1(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("----in work1, g_num is %d---" % g_num)


def work2(num):
    global g_num
    for i in range(num):
        g_num += 1
    print("----in work2, g_num is %d---" % g_num)


print("---线程创建之前g_num is %d---" % g_num)

t1 = threading.Thread(target=work1, args=(100,))
t1.start()

t2 = threading.Thread(target=work2, args=(100,))
t2.start()

while len(threading.enumerate()) != 1:
    time.sleep(1)

print("2个线程对同一个全局变量操作之后的最终结果是:%s" % g_num)
