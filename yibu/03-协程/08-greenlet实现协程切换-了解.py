import time
import greenlet # sudo pip3 install greenlet
# 为了更好使用协程来完成多任务，python中的greenlet模块对其封装，从而使得切换任务变的更加简单


def work2():
    while True:
        print("----work2---")
        g1.switch()
        time.sleep(0.5)

def work1():
    while True:
        print("----work1---")
        g2.switch()
        time.sleep(0.5)

if __name__ == '__main__':
    g1 = greenlet.greenlet(work1)
    g2 = greenlet.greenlet(work2)
    # 切换到第一个协程执行
    g1.switch()

# 需要自己手动g.switch()
# 切换到指定的协程 - 不爽