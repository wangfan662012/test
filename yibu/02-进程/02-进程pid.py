# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
from multiprocessing import Process
import time, os


def run_proc():
    '''子进程要执行的代码'''
    print("子进程中,pid=%d..." % os.getppid())  # os.getpid获取当前进程的进程号
    print("子进程将要结束...")


if __name__ == '__main__':
    print("父进程,pid=%d..." % os.getppid())  # os.getpid获取当前进程的进程号
    p = Process(target=run_proc)
    p.start()


