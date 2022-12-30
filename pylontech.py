import can
import cantools
from pprint import pprint
import time
import json
from datetime import date
from datetime import date, datetime
import paho.mqtt.client as paho
broker="192.168.5.12"
port=1883
dbcfile="/home/pi/pylontech.dbc"
caninterface="can0"

def on_publish(client,userdata,result):             #create function for callback
    print("mqtt published")
    pass

client1 = paho.Client("battery")                    #create client object
client1.on_publish = on_publish                     #assign function to callback
client1.connect(broker,port)                        #establish connect

# AlarmAndWarn
binary_sensor_topic_template = 'homeassistant/binary_sensor/battery/*/config'
binary_sensor_value_template = \
  '{\
  "name"          :"Battery *",\
  "unique_id"     :"battery_#_*",\
  "state_topic"   :"solar/battery/#",\
  "pl_on":"1","pl_off":"0",\
  "value_template":"{{ value_json.*}}",\
  "device"  :{"name":"battery","ids":"battery","cu":"http://solaranzeige.fritz.box","mf":"PYLON","mdl":"US2000, US3000, US5000","sw":"00000001"}\
  }'
  
ret = client1.publish( str(binary_sensor_topic_template).replace("*","Alarm_Over_Current_Discharge"), \
                      (str(binary_sensor_value_template).replace("*","Alarm_Over_Current_Discharge")).replace("#","BMS_Alarm_Warn"))
                      
ret = client1.publish( str(binary_sensor_topic_template).replace("*","Alarm_Under_Temperature"), \
                      (str(binary_sensor_value_template).replace("*","Alarm_Under_Temperature")).replace("#","BMS_Alarm_Warn"))   
                      
ret = client1.publish( str(binary_sensor_topic_template).replace("*","Alarm_Over_Temperature"), \
                      (str(binary_sensor_value_template).replace("*","Alarm_Over_Temperature")).replace("#","BMS_Alarm_Warn"))

ret = client1.publish( str(binary_sensor_topic_template).replace("*","Alarm_Under_Voltage"), \
                      (str(binary_sensor_value_template).replace("*","Alarm_Under_Voltage")).replace("#","BMS_Alarm_Warn"))

ret = client1.publish( str(binary_sensor_topic_template).replace("*","Alarm_Over_Voltage"), \
                      (str(binary_sensor_value_template).replace("*","Alarm_Over_Voltage")).replace("#","BMS_Alarm_Warn"))

ret = client1.publish( str(binary_sensor_topic_template).replace("*","Alarm_Internal"), \
                      (str(binary_sensor_value_template).replace("*","Alarm_Internal")).replace("#","BMS_Alarm_Warn"))

ret = client1.publish( str(binary_sensor_topic_template).replace("*","Alarm_Over_Current_Charge"), \
                      (str(binary_sensor_value_template).replace("*","Alarm_Over_Current_Charge")).replace("#","BMS_Alarm_Warn"))

ret = client1.publish( str(binary_sensor_topic_template).replace("*","Warn_High_Current_Discharge"), \
                      (str(binary_sensor_value_template).replace("*","Warn_High_Current_Discharge")).replace("#","BMS_Alarm_Warn"))

ret = client1.publish( str(binary_sensor_topic_template).replace("*","Warn_Low_Temperature"), \
                      (str(binary_sensor_value_template).replace("*","Warn_Low_Temperature")).replace("#","BMS_Alarm_Warn"))

ret = client1.publish( str(binary_sensor_topic_template).replace("*","Warn_High_Temperature"), \
                      (str(binary_sensor_value_template).replace("*","Warn_High_Temperature")).replace("#","BMS_Alarm_Warn"))

ret = client1.publish( str(binary_sensor_topic_template).replace("*","Warn_Low_Voltage"), \
                      (str(binary_sensor_value_template).replace("*","Warn_Low_Voltage")).replace("#","BMS_Alarm_Warn"))

ret = client1.publish( str(binary_sensor_topic_template).replace("*","Warn_High_Voltage"), \
                      (str(binary_sensor_value_template).replace("*","Warn_High_Voltage")).replace("#","BMS_Alarm_Warn"))

ret = client1.publish( str(binary_sensor_topic_template).replace("*","Warn_Internal"), \
                      (str(binary_sensor_value_template).replace("*","Warn_Internal")).replace("#","BMS_Alarm_Warn"))

ret = client1.publish( str(binary_sensor_topic_template).replace("*","Warn_High_Current_Charge"), \
                      (str(binary_sensor_value_template).replace("*","Warn_High_Current_Charge")).replace("#","BMS_Alarm_Warn"))
                                            
#  Charge 

ret = client1.publish( str(binary_sensor_topic_template).replace("*","Charge_Immediately"), \
                      (str(binary_sensor_value_template).replace("*","Charge_Immediately")).replace("#","BMS_Charge"))
                      
ret = client1.publish( str(binary_sensor_topic_template).replace("*","Discharge_Enable"), \
                      (str(binary_sensor_value_template).replace("*","Discharge_Enable")).replace("#","BMS_Charge"))                      
                      
ret = client1.publish( str(binary_sensor_topic_template).replace("*","Charge_Enable"), \
                      (str(binary_sensor_value_template).replace("*","Charge_Enable")).replace("#","BMS_Charge"))

# BMS_Battery  

sensor_topic_template = 'homeassistant/sensor/battery/*/config'
sensor_value_template = \
  '{\
  "name"          :"Battery *",\
  "unique_id"     :"battery_#_*",\
  "state_topic"   :"solar/battery/#",\
  "value_template":"{{ value_json.*}}",\
  "device"  :{"name":"battery","ids":"battery","cu":"http://solaranzeige.fritz.box","mf":"PYLON","mdl":"US2000, US3000, US5000","sw":"00000001"},\
  "expire_after":45,\
  "state_class":"measurement"\
  &\
  }'

BMS_parameters = ',\
  "device_class": "voltage",\
  "unit_of_measurement": "V",\
  "icon": "mdi:speedometer",\
  "min": 44.5, "max": 53.5'

ret = client1.publish( str(sensor_topic_template).replace("*","Battery_Voltage"), \
                      (str(sensor_value_template).replace("*","Battery_Voltage")).replace("#","BMS_Battery").replace("&",BMS_parameters))

BMS_parameters = ',\
  "device_class": "current",\
  "unit_of_measurement": "A",\
  "icon": "mdi:speedometer",\
  "min": -148, "max": 148'
   
ret = client1.publish( str(sensor_topic_template).replace("*","Battery_Current"), \
                      (str(sensor_value_template).replace("*","Battery_Current")).replace("#","BMS_Battery").replace("&",BMS_parameters))
                      
BMS_parameters = ',\
  "device_class": "temperature",\
  "unit_of_measurement": "°C",\
  "icon": "mdi:speedometer",\
  "min": 0, "max": 40'                      
                      
ret = client1.publish( str(sensor_topic_template).replace("*","Battery_Temperature"), \
                      (str(sensor_value_template).replace("*","Battery_Temperature")).replace("#","BMS_Battery").replace("&",BMS_parameters))

#  "entity_category": "config",

#  State  

BMS_parameters = ',\
  "device_class": "battery",\
  "unit_of_measurement": "%"'                      
                      
ret = client1.publish( str(sensor_topic_template).replace("*","SOC"), \
                      (str(sensor_value_template).replace("*","SOC")).replace("#","BMS_State").replace("&",BMS_parameters))

BMS_parameters = ',\
  "device_class": "battery",\
  "unit_of_measurement": "%"'                      
                      
ret = client1.publish( str(sensor_topic_template).replace("*","SOH"), \
                      (str(sensor_value_template).replace("*","SOH")).replace("#","BMS_State").replace("&",BMS_parameters))

#DC

BMS_parameters = ',\
  "device_class": "voltage",\
  "unit_of_measurement": "V"'

ret = client1.publish( str(sensor_topic_template).replace("*","Battery_Charge_Voltage"), \
                      (str(sensor_value_template).replace("*","Battery_Charge_Voltage")).replace("#","BMS_DC_Parameter").replace("&",BMS_parameters))

BMS_parameters = ',\
  "device_class": "current",\
  "unit_of_measurement": "A"'
   
ret = client1.publish( str(sensor_topic_template).replace("*","Charge_Current_Limitation"), \
                      (str(sensor_value_template).replace("*","Charge_Current_Limitation")).replace("#","BMS_DC_Parameter").replace("&",BMS_parameters))

BMS_parameters = ',\
  "device_class": "current",\
  "unit_of_measurement": "A"'
   
ret = client1.publish( str(sensor_topic_template).replace("*","Discharge_Current_Limitation"), \
                      (str(sensor_value_template).replace("*","Discharge_Current_Limitation")).replace("#","BMS_DC_Parameter").replace("&",BMS_parameters))
                      

db = cantools.database.load_file(dbcfile)
can_bus = can.interface.Bus(caninterface, bustype='socketcan')

while 1:
  message = can_bus.recv()

  canname =  (db.get_message_by_frame_id(message.arbitration_id).name)
  test = db.decode_message(message.arbitration_id, message.data)
  ret = client1.publish(str("solar/battery/")+canname,str(test).replace("'","\""))
