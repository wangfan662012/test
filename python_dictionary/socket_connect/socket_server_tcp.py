#非阻塞模块
import socketserver

#首先我们需要定义一个类
class MySocketServer(socketserver.BaseRequestHandler):
    #首先执行setup方法，然后执行handle方法，最后执行finish方法
    #如果handle方法报错，则会跳过
    #setup与finish无论如何都会执行
    #一般只定义handle方法即可
    def setup(self):
        pass

    def handle(self):
        #定义连接变量
        conn=self.request
        # 提示信息
        print("连接成功")
        #发送消息定义
        msg="Hello World!"
        #发送消息
        conn.send(msg.encode())
        #进入循环 不断接收客户端消息
        while True:
            #接收客户端消息
            data=conn.recv(1024)
            #打印消息
            print(data.decode())
            if data==b'exit':
                break
            conn.send(data)
        conn.close()

    def finish(self):
        pass

if __name__=='__main__':
    # 提示信息
    print("正在等待接收数据。。。。")
    #创建多线程实例
    server=socketserver.ThreadingTCPServer(("127.0.0.1",8888),MySocketServer)
    #开启异步多线程，等待连接
    server.serve_forever()