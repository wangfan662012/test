import yagmail
import schedule
import time

email_message = {
    'smtp_server':'smtp.qq.com',
    'from_user':'674246941@qq.com',
    'from_password':'vjqupbshxrflbeji',
    'to_user':'fwang@kaikeba.com',
    'subject':'python自动化测试',
    'contents':'邮件正文',
    'file_name':r'G:\Python_project\test\case\detaillist.xlsx'
}

def send_mail(smtp_server, from_user, from_password, to_user, subject, contents, file_name):
    # 初始化服务器等信息
    yag = yagmail.SMTP(from_user, from_password, smtp_server)
    # 发送邮件
    yag.send(to_user, subject, contents, file_name)


schedule.every().day.at("12:00").do(send_mail, **email_message)
while True:
    schedule.run_pending()
    time.sleep(1)

