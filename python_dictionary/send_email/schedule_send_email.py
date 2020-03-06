import requests
import smtplib
import schedule
import time
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

account = input('请输入你的邮箱：')
password = input('请输入你的密码：')
receiver = input('请输入收件人的邮箱：')
index = 0
# index的目的是让程序只运行两次就结束
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

def movie_spider():
    res_movies = requests.get('https://movie.douban.com/chart', headers=headers)
    bs_movies = BeautifulSoup(res_movies.text, 'html.parser')
    list_movies = bs_movies.find_all('div', class_='pl2')
    list_all = []
    for movie in list_movies:
        tag_a = movie.find('a')
        name = tag_a.text.replace(' ', '').replace('\n', '')
        # 电影名，使用replace方法去掉多余的空格及换行符
        url = tag_a['href']
        # 电影详情页的链接
        tag_p = movie.find('p', class_='pl')
        # 提取父级标签中的<p>标签
        information = tag_p.text.replace(' ', '').replace('\n', '')
        # 电影基本信息，使用replace方法去掉多余的空格及换行符
        tag_div = movie.find('div', class_='star clearfix')
        # 提取父级标签中的<div>标签
        rating = tag_div.text.replace(' ', '').replace('\n', '')
        # 电影评分信息，使用replace方法去掉多余的空格及换行符
        list_all.append(name + url + information + rating)
        # 将电影名、URL、电影基本信息和电影评分信息，封装为列表，用append方法添加进list_all
    return list_all

def send_email(movie_list):
    global account, password, receiver
    mailhost = 'smtp.qq.com'
    # qqmail = smtplib.SMTP()
    # qqmail.connect(mailhost, 25)
    qqmail = smtplib.SMTP_SSL()
    qqmail.connect(mailhost, 465)
    qqmail.login(account, password)
    content = '\n'.join(movie_list)
    print(content)
    message = MIMEText(content, 'plain', 'utf-8')
    subject = '本周豆瓣新片榜'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print('邮件发送成功')
    except:
        print('邮件发送失败')
    qqmail.quit()

def job():
    global index
    print('开始任务')
    movie_list = movie_spider()
    send_email(movie_list)
    print(movie_list)
    print('任务完成')
    index += 1

schedule.every().second.do(job)

while index!=2:
    # 这里会当index == 2的时候程序结束
    schedule.run_pending()
    time.sleep(1)