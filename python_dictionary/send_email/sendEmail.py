from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( Header(name, 'utf-8').encode(), addr))
# 输入Email地址和口令:
from_addr = '674246941@qq.com'
password = 'vjqupbshxrflbeji'
# 输入SMTP服务器地址:
smtp_server = 'smtp.qq.com'
# 输入收件人地址:
to_addr = ['fwang@kaikeba.com']
content = '''
亲爱的学员朋友：
    你好！
    恭喜大家学习坚持到现在!
    开课吧只为赋能人才，小课让学习更轻松！
'''

msg = MIMEText(content, 'plain', 'utf-8')
msg['From'] = _format_addr(u'开课吧 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自小K的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()