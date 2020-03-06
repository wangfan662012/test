# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
import time
import asyncio

now = lambda: time.time()


async def do_some_work(x):
    print("waiting:", x)


start = now()
# coroutine 协程:协程对象，指一个使用async关键字定影的函数
# 它的调用不会立即执行函数，而是会返回一个协程对象。
# 协程对象需要注册到事件循环，由事件循环调用。
coroutine = do_some_work(2)  # 这里是一个协程对象，这个时候do_some_work函数并没有执行
print(coroutine)

# 创建一个事件loop
# 将协程加入到事件循环loop
loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)
# event_loop 事件循环：程序开启一个无限循环，把一些函数注册到事件循环上，当满足事件发生时，调用响应的协程函数


'''
# 在上面代码中我们通过async关键字定义一个协程（coroutine）,
# 当然协程不能直接运行，需要将协程加入到事件循环loop中

# asyncio.get_event_loop：创建一个事件循环，
# 然后使用run_until_complete将协程注册到事件循环，并启动事件循环

# 关于asyncio的一些关键字的说明：

# event_loop 事件循环：程序开启一个无限循环，
# 把一些函数注册到事件循环上，当满足事件发生的时候，调用相应的协程函数

# coroutine 协程：协程对象，指一个使用async关键字定义的函数，
# 它的调用不会立即执行函数，而是会返回一个协程对象。
# 协程对象需要注册到事件循环，由事件循环调用。

# task 任务：一个协程对象就是一个原生可以挂起的函数，
# 任务则是对协程进一步封装，其中包含了任务的各种状态

# future: 代表将来执行或没有执行的任务的结果。
# 它和task上没有本质上的区别

# async/await 关键字：python3.5用于定义协程的关键字，
# async定义一个协程，await用于挂起阻塞的异步调用接口。
'''
