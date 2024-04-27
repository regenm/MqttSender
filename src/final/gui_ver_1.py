'''
* simplified version
* 
* 
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import mqttSender
import tkinter
import tkinter.scrolledtext

user_id=""                      # your mqtt account name         
user_pwd=""                     # your mqtt account password                                      
mqtt_server=""                  # your mqtt IP address or domain         
mqtt_clientID=""                # your unique client id         
mqtt_topic=""                   # the topic you want to send message


def send():
    var=content_tobe_sent.get()
    mqtt.sendMessage(mqtt_topic,var)
    var="message : "+var+"\n"
    output_text.insert("end",var)

mqtt=mqttSender.MqttSender(user_id=user_id,user_pwd=user_pwd,client_id=mqtt_clientID,mqtt_server=mqtt_server)
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

# mqtt.sendMessage("/mqttSender_test","gui_ver_1 test")











root.mainloop()