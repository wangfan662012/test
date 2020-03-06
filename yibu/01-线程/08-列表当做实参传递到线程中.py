# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
from threading import Thread
import time


def work1(nums):
    nums.append(44)
    print("----in work1---", nums)


def work2(nums):
    # 延时一会，保证t1线程中的事情做完
    time.sleep(1)
    print("----in work2---", nums)


g_nums = [11, 22, 33]

t1 = Thread(target=work1, args=(g_nums,))
t1.start()

t2 = Thread(target=work2, args=(g_nums,))
t2.start()

# 在一个进程内的所有线程共享全局变量，很方便在多个线程间共享数据
# 缺点就是，线程是对全局变量随意遂改可能造成多线程之间对全局变量的混乱（即非线程安全）
