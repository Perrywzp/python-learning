# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr

import smtplib, getpass


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('From: ')
password = getpass.getpass('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')


msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候。。。', 'utf-8').encode()

msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

with open('D:\\python-code\\python-learning\\blur.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是jpg类型
    mime = MIMEBase('image', 'jpeg', filename = 'blur.jpg')
    # 加上必要的头信息
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件内容读进来
    mime.set_payload(f.read())
    # 用base64编码
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)


server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
