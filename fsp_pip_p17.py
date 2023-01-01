import serial
import time
import json
from datetime import date
from datetime import datetime
import paho.mqtt.client as paho
broker="192.168.5.12"
port=1883
topic = str("solar/wr/power")

def on_publish(client,userdata,result):             #create function for callback
    print("mqtt published \n")
    pass

ser = serial.Serial()
ser.baudrate = 2400
ser.port = '/dev/ttyUSB0'
ser.bytesize= 8
ser. parity= 'N'
ser.stopbits= 1
ser.open()

data = {}

def on_publish(client,userdata,result):             #create function for callback
    print("mqtt published")
    pass


client1= paho.Client("wr0")                           #create client object
client1.on_publish = on_publish                       #assign function to callback
client1.connect(broker,port)                          #establish connect

sensor_topic_template = 'homeassistant/sensor/wr/*/config'
sensor_value_template = \
  '{\
  "name"          :"WR *",\
  "unique_id"     :"wr_#_*",\
  "state_topic"   :"solar/wr/#",\
  "value_template":"{{ value_json.*}}",\
  "device"  :{"name":"wr","ids":"wr","cu":"http://solaranzeige.fritz.box","mf":"FSP","mdl":"PowerManager-Hybrid 10kW","sw":"00000001"},\
  "expire_after":45,\
  "state_class":"measurement"\
  &\
  }'
  
parameters = ',\
  "device_class": "power",\
  "unit_of_measurement": "W",\
  "icon": "mdi:speedometer",\
  "min": -10000, "max": 10000'

ret = client1.publish( str(sensor_topic_template).replace("*","DefFeedInPow"), \
                      (str(sensor_value_template).replace("*","DefFeedInPow")).replace("#","power").replace("&",parameters))

ret = client1.publish( str(sensor_topic_template).replace("*","ActPvPow"), \
                      (str(sensor_value_template).replace("*","ActPvPow")).replace("#","power").replace("&",parameters))
                      
ret = client1.publish( str(sensor_topic_template).replace("*","ReservPow"), \
                      (str(sensor_value_template).replace("*","ReservPow")).replace("#","power").replace("&",parameters))  

ret = client1.publish( str(sensor_topic_template).replace("*","ActFeedPow"), \
                      (str(sensor_value_template).replace("*","ActFeedPow")).replace("#","power").replace("&",parameters))  

parameters = ',\
  "unit_of_measurement": "%",\
  "icon": "mdi:speedometer",\
  "min": 0, "max": 150'

ret = client1.publish( str(sensor_topic_template).replace("*","LoadFactor"), \
                      (str(sensor_value_template).replace("*","LoadFactor")).replace("#","power").replace("&",parameters))

previous = datetime.now();
now = datetime.now()

while True:
	ser_bytes = ser.read_until(b'\r')
	now = datetime.now()	
	string = str(ser_bytes)
	txt = string.split(",")
#	print (len(txt),txt[0])  
	if(len(txt) == 6):
		value = '{'+\
			'"Time": '+'"'+str(now).replace(" ", "T")+'"'+','+\
			'"DefFeedInPow": '      +str(int(txt[1]))+','+\
	                '"ActPvPow": '+str(int(txt[2]))+','+\
	                '"ActFeedPow": '   +str(int(txt[3]))+','+\
	                '"LoadFactor": '+str(float(int(txt[2])) /float(int(txt[4])))+','+\
	                '"ReservPow": '   +str(int(txt[4]))+\
	                '}'
	                
	                			  
		if ((now-previous).total_seconds() >= 5):  # WR offers values after 1..7s - stabilize a bit bei rejecting 

			ret = client1.publish(topic, value)
#			print (txt[0], value, txt[5]) 
			previous = now
ser.close()

