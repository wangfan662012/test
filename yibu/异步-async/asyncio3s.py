# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
import threading
import asyncio


async def hello():
    print('hello world! (%s)' % threading.current_thread())
    await asyncio.sleep(1)
    print('hello again! (%s)' % threading.current_thread())


def runeventloop():
    loop = asyncio.new_event_loop()
    tasks = [hello(), hello()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    runeventloop()
    asyncio.set_event_loop(loop)


