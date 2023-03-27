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
#print('network config:', wlan.ifconfig())
macAdd=wlan.config('mac')
topico=(binascii.hexlify(macAdd).decode('utf-8'))
    

rs232=machine.UART(2,115200)
#btn=Pin(0)
led=Pin(2, Pin.OUT)
trig=Pin(33, Pin.OUT)

def interaction(topic, msg):
    if msg==b'accesoOK':        
        led.value(1)
        trig.value(0)
        time.sleep_ms(100)       
        led.value(0)
        trig.value(1)


                    #clientid,host
mqttc = MQTTClient(topico,'mkt.local')
mqttc.connect()
mqttc.set_callback(interaction)
mqttc.subscribe(topico) #topic

#macAdd=do_connect()
while True:
    time.sleep_ms(500)
    rs232.write(b'\x0A\xFF\x09\x88\x00\x00\x00\x00\x01\x02\x06\x5d')
    read232=rs232.readline()    
    if read232 != b'\x0b\xc8\x02\x05&' and read232 is not None:
        decoTag=binascii.hexlify(read232).decode('utf-8')
        mqttc.publish('dxtr',(decoTag+topico)[15:])
    mqttc.check_msg()
    
    
    

