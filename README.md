# PylontechUSX00C_CAN2MQTT
Get CAN-Messages from Pytontech BMS and send as MQTT to Homeassistant.

I did the scripting for my four Pylontech US3000C polled by a RPi4, but it should work for others, too.
I'm a very beginner regarding python and HA...

A small python script listens to the CAN messages, decodes it by using can/cantools and
a *.dbc file I created from the latest(?) Pylontech documentations and publishes the
messages as MQTT. It doesn't do any comfort or error handling. You even have to put
the MQTT host into the file (not a parameter).

Pylontech uses CAN with 500.000 bps by default. You can view the CAN messages comming to 
the interface using candump can0 and don't have to sent anything (or equivalent, 
depending on hardware). Some Inverters are polling aditional data, mine does not.
Via CAN you can't see the single cell voltages. I'll probably do an other script for
RS-485 or RS-232 interface in future.

The *dbc is the CAN data description for the can messages on bus. The IDs are in decimal there.
DBC definition is owned by a company and explanaitions are various but none is really complete
it seems. 

For homeassistant's auto-detect of "Devices and Entities" the python script generates the 
config MQTT messages, too. Automatic import doesn't place the topics ordered or grouped so 
I manually placed them in my prefered order and grouped them inside HA.

Since HA showed floats not rounded and power and energy "flow" I found missing, I added 
template-sensors in the global template.yaml of HA and used them in the HA card 
(see: template.yaml and example.yaml).

I didn't activate the retain-flag in the python up to now since for my understanding 
this makes it uncomfortable to get rid of the topics when trying things out.
When the script starts up again (used a service at linux) they are back again, too.

# Credits
Direct thanks to the guys who did OpenDTU for the Hoymiles HM-xxxx solar inverters which I studied
and used as the example to get the HA integration done.
