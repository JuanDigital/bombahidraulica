#espBlood.py
import network
import machine
import time
from umqtt.simple import MQTTClient
from machine import Pin
import binascii

wlan = network.WLAN(network.STA_IF)
if not wlan.isconnected():
    wlan.active(True)
    wlan.connect('PlantaAlta', 'xya8G39ecK')
    while not wlan.isconnected():
        pass

led=Pin(2, Pin.OUT)
trig=Pin(33, Pin.OUT)

def interaction(topic, msg):
    if msg==b'encender':        
        led.value(1)
        trig.value(0)
    elif msg== b'apagar'      
        led.value(0)
        trig.value(1)


                    #clientid,host
mqttc = MQTTClient('espChido','192.168.1.x')
mqttc.connect()
mqttc.set_callback(interaction)
mqttc.subscribe('control') #topic

#macAdd=do_connect()
while True:
    mqttc.check_msg()
    
    
    

