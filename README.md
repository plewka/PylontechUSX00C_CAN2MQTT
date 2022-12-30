# PylontechUSX00C_CAN2MQTT
Get CAN-Messages from Pytontech BMS and send as MQTT to Homeassistant

I did it for my four Pylontech US3000C polled by a RPi4, but it should work for others, too.

A small python script listens to the CAN messages, decodes it by using can/cantools and
a *.dbc file I created from the latest(?) Pylontech documentations and publishes the
messages as MQTT.

For homeassistant's auto-detect of Device and Entities the script generates the 
config MQTT messages, too.

Since HA showed floats not rounded and power and energy "flow" were missing, I added 
template-sensors and used them in the HA card. 

I didn't activate the retain-flag up to now since it's difficult to get rid of the messages
when trying things out.

# Credits
Direct thanks to the guys who did OpenDTU for the Hoymiles HM-xxxx solar inverters which I studied
and used as the example to get the HA integration done.
