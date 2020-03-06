# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
import threading, time


class MyThred(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            data = "我是线程：{a}  @  {b}".format(a=self.name, b=i)  # name属性中保存的是当前线程的名字
            print(data)


def test():
    for i in range(5):
        t = MyThred()
        t.start()


if __name__ == '__main__':
    # t = MyThred()
    # t.start()
    test()

# 从代码和执行结果我们可以看出，多线程程序的执行顺序是不确定的。
# 当执行到sleep语句时，线程将被阻塞（Blocked），到sleep结束后，线程进入就绪（Runnable）状态，等待调度。
# 而线程调度将自行选择一个线程执行。上面的代码中只能保证每个线程都运行完整个run函数，但是线程的启动顺序、run函数中每次循环的执行顺序都不能确定。


