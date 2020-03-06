"""
greenlet已经实现了协程，但是这个还的人工切换，是不是觉得太麻烦了，不要捉急，
python还有一个比greenlet更强大的并且能够自动切换任务的模块gevent

其原理是当一个greenlet遇到IO(指的是input output 输入输出，比如网络、文件操作等)操作时，
比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。

由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO
"""
from gevent import monkey  # pip3 install gevent

monkey.patch_all()
# 将网络IO 时间 recv accpt time.sleep()默认会阻塞的一些事件 变为非阻塞; 实现多任务的自动切换
# 官方文档 补丁必须在前两行
import gevent
import time


# from gevent import monkey   # pip3 install gevent
# monkey.patch_all()

def work2():
    while True:
        print("----work2---")
        gevent.sleep(0.5)
        time.sleep(0.5)


def work1():
    while True:
        print("----work1---")
        gevent.sleep(0.5)
        time.sleep(0.5)


if __name__ == '__main__':
    # 创建协程 并且 启动执行
    g1 = gevent.spawn(work1)
    g2 = gevent.spawn(work2)

    # 等待协程执行完成
    g1.join()
    g2.join()

    # 等待所有协程执行完成
    # gevent.joinall([g1, g2])

for i in range(3):
    print(i)
