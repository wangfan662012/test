# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
from multiprocessing import Process
import time


def run_proc():
    '''子进程要执行的代码'''
    while True:
        print("---2---")
        time.sleep(1)


if __name__ == '__main__':
    p = Process(target=run_proc)
    p.start()
    while True:
        print("---1---")
        time.sleep(1)

# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动
