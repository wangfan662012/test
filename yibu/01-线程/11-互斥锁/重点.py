# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
'''
互斥锁
当多个线程几乎同时修改某一个共享数据的时候，需要进行同步控制

线程同步能够保证多个线程安全访问竞争资源，最简单的同步机制是引入互斥锁。

互斥锁为资源引入一个状态：锁定/非锁定

某个线程要更改共享数据时，先将其锁定，此时资源的状态为“锁定”，其他线程不能更改；
直到该线程释放资源，将资源的状态变成“非锁定”，其他的线程才能再次锁定该资源。互斥锁保证了每次只有一个线程进行写入操作，从而保证了多线程情况下数据的正确性。
'''
# threading模块中定义了Lock类，可以方便的处理锁定：
# # 创建锁
# mutex = threading.Lock()
# # 锁定
# mutex.acquire()
# # 释放
# mutex.release(）
# 注意：
# 如果这个锁之前是没有上锁的，那么acquire不会堵塞
# 如果在调用acquire对这个锁上锁之前 它已经被 其他线程上了锁，那么此时acquire会堵塞，直到这个锁被解锁为止


# 使用互斥锁完成2个线程对同一个全局变量各加100万次的操作
import threading
import time

g_num = 0


def test1(num):
    global g_num
    for i in range(num):
        mutex.acquire()  # 上锁
        g_num += 1
        mutex.release()  # 解锁

    print("---test1---g_num=%d" % g_num)


def test2(num):
    global g_num
    for i in range(num):
        mutex.acquire()  # 上锁
        g_num += 1
        mutex.release()  # 解锁

    print("---test2---g_num=%d" % g_num)


# 创建一个互斥锁
# 默认是未上锁的状态
mutex = threading.Lock()

# 创建2个线程，让他们各自对g_num加1000000次
p1 = threading.Thread(target=test1, args=(1000000,))
p1.start()

p2 = threading.Thread(target=test2, args=(1000000,))
p2.start()

# 等待计算完成
while len(threading.enumerate()) != 1:
    time.sleep(1)

print("2个线程对同一个全局变量操作之后的最终结果是:%s" % g_num)


# 当一个线程调用锁的acquire()方法获得锁时，锁就进入“locked”状态。
# 每次只有一个线程可以获得锁。如果此时另一个线程试图获得这个锁，该线程就会变为“blocked”状态，称为“阻塞”，直到拥有锁的线程调用锁的release()方法释放锁之后，锁进入“unlocked”状态。
# 线程调度程序从处于同步阻塞状态的线程中选择一个来获得锁，并使得该线程进入运行（running）状态。

# 总结
# 锁的好处：
# 确保了某段关键代码只能由一个线程从头到尾完整地执行
# 锁的坏处：
# 阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了
# 由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁
