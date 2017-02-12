# Raspberry Pi Weather Station

The code here will generally be a modification of the
Raspberry Pi Foundation Weather Station Code, I am not using the
official Raspberry Pi Weather Station hardware, so I will be
modifying it to suit my own hardware

Depends
* gpiozero

    sudo pip3 install gpiozero

* RPi.GPIO

    sudo pip3 install RPi.GPIO

* thingspeak

    sudo pip3 install thingspeak



## wind_direction.py

First up is the wind vane, this uses a Maplin wind vane, more specifically,
this [one](http://www.maplin.co.uk/p/maplin-replacement-wind-direction-sensor-for-n96fyn96gy-n81nf).

This is an analogue sensor and thus needs an Analogue to digital convertor or ADC.
The ADC I am using is an MCP3008, and to make it easy I am using the Rasp.io
[anglogzero](http://rasp.io/analogzero/) board by Alex Eames

This code has been updated to use the MCP3008 with [gpiozero](https://www.raspberrypi.org/blog/gpio-zero-a-friendly-python-api-for-physical-computing/)

## wind_direction.json

This file acts as a look up to convert the analogue sensor reading into either
a compass direction, i.e. NE, NNE, SW, etc. or a bearing, i.e. 45 degrees, 22.5 degrees, or 225 degrees.  When creating the wind_direction object in the wind_direction.py file, this json file is read into memory, additional information is added, which depend upon the ```vin``` and
```vdivider``` variable.

For the MCP3008 on the analogzero board ```vin``` should be set to 3.3v.  ```vdivider``` should be set to match the value of the voltage divider resister you are using.  In my case this is a 9.82kOhms or 9820 ohms.

## config.py

Add your thingspeak channel ID and read/write API keys in here

## interrupt_client.py

This is a direct copy of the Raspberry Pi Foundations' code, with a minor edit to get it working with Python3, the reset() method has been edited, if you are still using Python2 then remove the 'b' from before "RESET"

## interrupt_daemon.py

This is a direct copy of the Raspberry Pi Foundations' code.
Note, 

* the rain gauge uses BCM pin 6
* the wind speed gauge uses BCM pin 5

These can be changed in the setup() function.

For the sensors to work this must be called (and runs in the background using the following command:

    python3 interrupt_daemon.py start

If you want to restart it, the command is:

    python3 interrupt_daemon.py restart

If you want to stop the daemon running use:

    python3 interrupt_daemon.py stop

##log_all_sensors.py

This is based on the Raspberry Pi Foundations' code but has been heavily modified, all references to the Oracle database have been removed and I have added in the code to upload the data to thingspeak.
