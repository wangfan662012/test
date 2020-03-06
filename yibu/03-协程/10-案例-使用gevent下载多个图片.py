from gevent import monkey
monkey.patch_all()  # 自动切换

import gevent
import urllib.request
import time


def down_img(url):
    "图片网址https://rpic.douyucdn.cn/asrpic/181031/5732086_5800183_33698_2_2303.jpg"
    # 响应对象( 其中有图片数据)
    file_name = url[url.rfind("/") + 1:]
    print("开始下载图片%s" % file_name)
    response = urllib.request.urlopen(url)
    print("下载完成%s" % file_name)
    with open(file_name, "wb") as file:
        # 读取出图片数据 写入文件中
        file.write(response.read())

if __name__ == '__main__':
    # 1创建协程并且启动
    url_list = [
        "https://rpic.douyucdn.cn/asrpic/181031/5732086_5800183_33698_2_2303.jpg",
        "https://rpic.douyucdn.cn/asrpic/181031/4680635_3741595_2dc5f_2_2253.jpg",
        "https://rpic.douyucdn.cn/asrpic/181031/5580949_5798556_5a17b_2_2252.jpg"
    ]
    begin = time.time()
    # for url in url_list:
    g1 = gevent.spawn(down_img, url_list[0])
    g2 = gevent.spawn(down_img, url_list[1])
    g3 = gevent.spawn(down_img, url_list[2])

    # 2 等待任务执行完成
    gevent.joinall([g1, g2, g3])
    end = time.time()
    print("花费了%f秒" % (end - begin))