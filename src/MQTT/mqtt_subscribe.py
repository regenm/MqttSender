# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import random
 
def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))
 
 
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
 
 
#   订阅回调
def on_subscribe(client, userdata, mid, granted_qos):
    print("On Subscribed: qos = %d" % granted_qos)
    pass
 
 
#   取消订阅回调
def on_unsubscribe(client, userdata, mid):
    print ("取消订阅")
    print("On unSubscribed: qos = %d" % mid)
    pass
 
 
#   发布消息回调
def on_publish(client, userdata, mid):
    print ("发布消息")
    print("On onPublish: qos = %d" % mid)
    pass
 
 
#   断开链接回调
def on_disconnect( client, userdata, rc):
    print("断开链接") 
    print("Unexpected disconnection rc = " + str(rc))
    pass
 
client_id = "desktop client nh55"	# 生成一个设备号
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,client_id)
client.username_pw_set("regen", "regen")
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.on_disconnect = on_disconnect
client.on_unsubscribe = on_unsubscribe
client.on_subscribe = on_subscribe
client.connect('142.171.33.151', 1883, 600) # 600为keepalive的时间间隔
client.subscribe('/mqttSender_test', qos=0)
client.loop_forever() # 保持连接