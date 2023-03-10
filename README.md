# PylontechUSX00C_CAN2MQTT
Get CAN-Messages from Pytontech BMS and send as MQTT to Homeassistant.

I did the scripting for my four Pylontech US3000C polled by a RPi4, but it should work for others, too.

I added a script to sniff RS-485 communication of my FSP/MPP/Infini Hybrid 10k Solar Inverter.
Because I unfortunately I can't use these projects:

* https://github.com/cspiel1/fspctl
* https://github.com/search?q=mppsolar

I'm using the configuration which does the main communication
via the RS-232-Modbus-Link preventing an (additional) Modbus-Master an RS-485:  

* Dual ModBus Box Modbus RTU (P17) Card  
* PlexLog DataLogger
* SDM630

# Details
A small python script listens to the CAN messages, decodes it by using can/cantools and
a *.dbc file I created from the latest(?) Pylontech documentations and publishes the
messages as MQTT. It doesn't do any comfort or error handling. You even have to put
the MQTT host into the file (not a parameter).

Pylontech uses CAN with 500.000 bps by default. You can view the CAN messages comming to 
the interface using

* sudo ip link set can0 up type can bitrate 500000
* candump can0  (or equivalent, depending on hardware) 

and don't have to sent anything. Some Inverters are polling aditional data, mine does not.
Via CAN you can't see the single cell voltages. I'll probably do an other script for
RS-485 or RS-232 interface in future.

The *dbc is the CAN data description for the can messages on bus. The IDs are in decimal there.
DBC definition is owned by a company and explanations are various but none is really complete
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
# File use on converter server
* pylontech.py  python-script - I placed it at /home/pi/
* pylontech.dbc can-packet/data description - I placed it at /home/pi/
* battery.service systemd linux service - placed to /etc/systemd/system/

# File use on ha server
* template.yaml - after modification of ha.yaml located in main directory, edited with ha's file editor 
* example.yaml - sniplet from one of my solar dashboards 
* ha_pylontech_screenshoot.png - how it looks inside my ha

# Credits
Direct thanks to the guys who did OpenDTU for the Hoymiles HM-xxxx solar inverters which I studied
and used as the example to get the HA integration done. Many thanks to all the people which made it 
possible to have this great smart-home solution based on open source.
