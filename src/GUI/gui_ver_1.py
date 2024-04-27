'''
* simplified version
* 
* 
'''

'''
* simplified version
* 
* 
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter
import tkinter.scrolledtext



def send():
    pass
# GUI

root=tkinter.Tk()
root.title('mqttSender Version 1.0')   #标题
content_tobe_sent=tkinter.Entry(root) # input
button_send=tkinter.Button(root, text='send',command=send) # send button
output_text=tkinter.scrolledtext.ScrolledText(root, width=40, height=10) # output
content_tobe_sent.pack()
button_send.pack()
output_text.pack()
root.mainloop()

