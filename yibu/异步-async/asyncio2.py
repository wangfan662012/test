# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
import asyncio


@asyncio.coroutine
def hello():
    print("hello world")
    r = yield from asyncio.sleep(1)
    print("hello again!")


loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()

# asyncio的编程模型就是一个消息循环。
# 我们从asyncio模块中直接获取一个EventLoop的引用，
# 然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。

# @asyncio.coroutine把一个generator标记为coroutine类型，然后，
# 我们就把这个coroutine扔到EventLoop中执行。

# hello()会首先打印出Hello world!，
# 然后，yield from语法可以让我们方便地调用另一个generator。
# 由于asyncio.sleep()也是一个coroutine，
# 所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。
# asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），
# 然后接着执行下一行语句。
# 把asyncio.sleep(1)看成是一个耗时1秒的IO操作，
# 在此期间，主线程并未等待，
# 而是去执行EventLoop中其他可以执行的coroutine了，
# 因此可以实现并发执行。
