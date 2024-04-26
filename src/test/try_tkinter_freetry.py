'''
* simplified version
* 
* 
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter
import tkinter.messagebox
import tkinter.scrolledtext

def send():
    print("send message successfully")
def rootSettings(root):
    root.title('mqttSender')#标题
    root.geometry('600x400')#窗体大小
    root.resizable(False, False)#固定窗体



root=tkinter.Tk()
rootSettings(root)

input_text=tkinter.scrolledtext.ScrolledText(root, width=40, height=10).pack()
output_text=tkinter.scrolledtext.ScrolledText(root, width=40, height=10).pack()

button_send=tkinter.Button(root, text='send',command=send).pack()










root.mainloop()