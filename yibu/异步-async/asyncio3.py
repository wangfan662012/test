# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
import asyncio
import time


@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1)
    step = yield from asyncio.sleep(1)
    print("Hello again!")


# 获取Evenloop
loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 执行Evenloop
# loop.run_until_complete(hello())
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
