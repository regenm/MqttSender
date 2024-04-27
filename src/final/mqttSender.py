# -*- coding: utf-8 -*-# -*- coding: utf-8 -*-


import random
import paho.mqtt.client as mqtt

class MqttSender:
    client = mqtt.Client()

    def __init__(
            self,
            user_id:str,
            user_pwd:str,
            client_id:str,
            mqtt_server:str,
        ) -> None:
        self.client.__init__(mqtt.CallbackAPIVersion.VERSION1,client_id)
        self.fclient.username_pw_set(user_id, user_pwd)
        self.client.connect(mqtt_server, 1883, 600) # 600为keepalive的时间间隔
        self.client.on_connect = on_connect
        self.client.on_message = on_message
        self.client.on_publish = on_publish
        self.client.on_disconnect = on_disconnect
        self.client.on_unsubscribe = on_unsubscribe
        self.client.on_subscribe = on_subscribe
    def sendMessage(self,message):
        self.client.publish(topic='/mqttSender_test', payload=message, qos=0, retain=False)
        






def on_connect(client, userdata, flags, rc):
        print("链接")
        print("Connected with result code: " + str(rc))
 
 
def on_message(client, userdata, msg):
    print ("消息内容")
    print(msg.topic + " " + str(msg.payload))


#   订阅回调
def on_subscribe(client, userdata, mid, granted_qos):
    print ("订阅")
    print("On Subscribed: qos = %d" % granted_qos)
    pass


#   取消订阅回调
def on_unsubscribe(client, userdata, mid, granted_qos):
    print ("取消订阅")
    print("On unSubscribed: qos = %d" % granted_qos)
    pass


#   发布消息回调
def on_publish(client, userdata, mid):
    print ("发布消息")
    print("On onPublish: qos = %d" % mid)
    pass


#   断开链接回调
def on_disconnect(client, userdata, rc):
    print ("断开链接")
    print("Unexpected disconnection rc = " + str(rc))
    pass

