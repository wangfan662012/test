# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang


import asyncio


async def main():
    print("hello ...")
    await asyncio.sleep(1)
    # async/await 关键字：python3.5用于定义协程的关键字，
    # async定义一个协程，await用于挂起阻塞的异步调用接口。
    print("... world!")


asyncio.run(main())
