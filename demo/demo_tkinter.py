#coding:utf8
import tkinter as tk
window = tk.Tk()
window.title('邮件群发机(微信：dy94941)')
window.geometry('800x500')

label_from_addr = tk.Label(window, text='发件人地址', bg='gray', font=('宋体', 16), width=10, height=1)
label_from_addr.pack()  # 将小部件放置到主窗口中


button_transfer = tk.Button(window, text="发送", command=None)
button_transfer.pack()

window.mainloop()  # 进入消息循环