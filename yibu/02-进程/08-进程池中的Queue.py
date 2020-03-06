# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
# 如果要使用Pool创建进程，就需要使用multiprocessing.Manager()中的Queue()，
# 而不是multiprocessing.Queue()，否则会得到一条如下的错误信息：
# RuntimeError: Queue objects should only be shared between processes through inheritance.
from multiprocessing import Manager, Pool
import time, os, random


def reader(q):
    print("reader启动（%s）,父进程为（%s）" % (os.getpid(), os.getpid()))
    for i in range(q.qsize()):
        print("reader从Queue获取到的消息：%s" % q.get(True))


def writer(q):
    print("writer启动（%s）,父进程为（%s）" % (os.getpid(), os.getpid()))
    for i in "hello":
        q.put(i)


if __name__ == '__main__':
    print("(%s) start " % os.getpid())
    q = Manager().Queue()  # 使用Manager中的Queue
    po = Pool()  # 定义一个进程池
    po.apply_async(writer, (q,))
    time.sleep(1)  # 先让上面的任务向Queue存入数据，然后再让下面的任务开始从中取数据
    po.apply_async(reader, (q,))
    po.close()
    po.join()
    print("(%s) end " % os.getpid())
