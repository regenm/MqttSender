'''
* simplified version
* 
* 
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import mqttSender
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
content_tobe_sent=tkinter.Entry(root).pack(side='left') # input
button_send=tkinter.Button(root, text='send',command=send).pack(side='right') # send button
output_text=tkinter.scrolledtext.ScrolledText(root, width=40, height=10).pack() # output

mqtt=mqttSender.MqttSender("regen","regen","NH55","142.171.33.151")
mqtt.sendMessage("/mqttSender_test","gui_ver_1 test")










root.mainloop()