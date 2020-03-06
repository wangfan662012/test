# encoding: utf-8
from python_dictionary.juke_preform import data_juke, juke_socket
import threading


mobiles = data_juke.get_phone()
print(len(mobiles))


def loop(phone, trend_no):
    print('thread %s is running...' % threading.current_thread().name)
    count = len(mobiles)
    if n < count:
        print('thread %s >>> %s' % (threading.current_thread().name), trend_no)
        #juke_socket.token = data_juke.get_token(mobiles[0][0])
        juke_socket.token = data_juke.get_token(phone[0])
        juke_socket.stat_main()
    print('thread %s ended.' % threading.current_thread().name)


if __name__ == '__main__':
    n = 0
    for phone in mobiles:
        n = n+1
        t = threading.Thread(target=loop,  name='LoopThread', kwargs={"phone": phone, "trend_no": n})
        t.start()
        # t.join()
        print('thread %s ended.' % threading.current_thread().name)
