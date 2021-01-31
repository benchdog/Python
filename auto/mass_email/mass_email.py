#coding:utf8
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

import tkinter as tk
window = tk.Tk()
window.title('邮件群发机(微信：dy94941)')
window.geometry('600x400')

from_addr = "matt@baidu.com"
smtp_server = "127.0.0.1"
smtp_user = 'mask@ivy.org' #机关：该名字关联微信或者qq、或者指向某一链接
#点击"发送"按钮时，可添加几个“url链接”
smtp_psd = '123456'

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = 'Python爱好者 <%s>'.format(from_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

def transfer(to_addr_list, smtp_user, msg):
    for to_addr in to_addr_list:
        msg['To'] = '管理员 <%s>'.format(to_addr)
        try:
            # server.sendmail(smtp_user, [to_addr], msg.as_string())
            server.sendmail(smtp_user, to_addr, msg.as_string())
        except Exception as e:
            print('发送' + str(to_addr) + '失败：' + str(e))
            continue

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(smtp_user, smtp_psd)



label_from_addr = tk.Label(window, text='发件人地址', bg='gray', font=('宋体', 16), width=10, height=1)
label_from_addr.pack()  # 将小部件放置到主窗口中


button_transfer = tk.Button(window, text="发送", command=transfer)
button_transfer.pack()

window.mainloop()  # 进入消息循环
server.quit()