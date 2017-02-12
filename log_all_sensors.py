#!/usr/bin/python3

#import interrupt_client, MCP342X, wind_direction, HTU21D, bmp085, tgs2600, ds18b20_therm
import time
import interrupt_client
import wind_direction
import thingspeak
import config


FREQUENCY = 60 * 1 #Record data to thingspeak at this frequency

wind_dir = wind_direction.wind_direction(adc_channel = 7, config_file="wind_direction.json")
interrupts = interrupt_client.interrupt_client(port = 49501)


#-------
#Below here to be edited to upload to thingspeak
#-------

#wind_average = wind_dir.get_value(1) #ten seconds

print("Inserting...")
def publish(channel):

	try:
		response = channel.update({1:wind_average, 
					2:interrupts.get_wind(),
					3:interrupts.get_wind_gust(),
					4:interrupts.get_rain()})
		print("Data uploaded to thingspeak")
	except:
		print("connection failed")



if __name__ == "__main__":

	channel = thingspeak.Channel(id=config.channel_id,
				write_key=config.write_key)
	while True:
		'''
		Send channels to thingspeak
		'''
		wind_average = wind_dir.get_value(1) #ten seconds
		publish(channel)
	
		print("Wind direction = {0} Wind speed = {1} Wind gust = {2} Rain Fall = {3}".format(wind_average,
			interrupts.get_wind(), 
			interrupts.get_wind_gust(), 
			interrupts.get_rain()))
		print("done")
		interrupts.reset()
		time.sleep(FREQUENCY)
	
