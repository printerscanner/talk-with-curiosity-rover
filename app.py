import json
import requests
import datetime
import time
from threading import Thread


response = requests.get('http://marsweather.ingenology.com/v1/latest/')
json_data = json.loads(response.text)



low_temp = json_data['report']['min_temp_fahrenheit']
high_temp = json_data['report']['max_temp_fahrenheit']
conditions = json_data['report']['atmo_opacity']
sunset = json_data['report']['sunset'][11:-1]
month = json_data['report']['season']
sol = json_data['report']['sol']

def sleeper():
	time.sleep(.5)
	print "..."
	time.sleep(.5)
	


def curiosity():
	sleeper()
	sleeper()
	print('''
	
			      O   O	
			    [________]				
			   _ _ _ _ _ _
				|		  
				|		  
				|		  
			   -|- - - - -|-		
			  -   -	    -   -
			 - - - -   - - - - 
			
			 									''')
	time.sleep(2)
	print "Transmitting from Curiosity Rover. It's sol", sol, "on Mars. Please come get me!"

	sleeper()

def weather_report(low_temp,high_temp,conditions):
	time.sleep(1)
	print " "
	print "Today's Weather Report:"

	time.sleep(2)
	print "Lows from", low_temp, "F"
	time.sleep(2)
	print "Highs from:", high_temp, "F"
	time.sleep(2)
	print "Conditions favor", conditions,"skies" 


def sunset_mars(sunset):
	time.sleep(2)
	print "Sunset on Mars:", sunset


def coldest_temp():
	# time.sleep(2)
	total = 0
	date = ""
	for i in range(1,93):
		# arr = ['http://marsweather.ingenology.com/v1/archive/?page=1']
		response = requests.get('http://marsweather.ingenology.com/v1/archive/?page=%d' % (i))
		json_data = json.loads(response.text)
		# arr.append(json_data['next'])
		for i in range(1,9):
			if json_data['results'][i]['min_temp_fahrenheit'] < total:
				total = json_data['results'][i]['min_temp_fahrenheit']
				date = json_data['results'][i]['terrestrial_date']
	print "The coldest temperature I've recorded is,", total, "F, on",  date


def warmest_temp():
	time.sleep(2)
	total = 0
	date = ""
	for i in range(1,93):
		# arr = ['http://marsweather.ingenology.com/v1/archive/?page=1']
		response = requests.get('http://marsweather.ingenology.com/v1/archive/?page=%d' % (i))
		json_data = json.loads(response.text)
		# arr.append(json_data['next'])
		for i in range(1,9):
			if json_data['results'][i]['max_temp_fahrenheit'] > total:
				total = json_data['results'][i]['max_temp_fahrenheit']
				date = json_data['results'][i]['terrestrial_date']
	print "The warmest temperature I've recorded is,", total, "F, on",  date
	end_transmission()
	

def current_time():
	time.sleep(2)
	currentDT = datetime.datetime.now()
	print "Current Time on Earth:", (currentDT.strftime("%I:%M:%S"))
	

def sunset_time():
	time.sleep(2)
	currentDT = datetime.datetime.now()
	a,b,c = sunset.split(":")
	d,e,f = (currentDT.strftime("%I:%M:%S")).split(":")
	print "Sunset on Mars in:", int(a) - int(d), "Hours"


def season_calculator(month):
	time.sleep(2)
	month_number = int(month[6:])
	season = ""
	if month_number < 6.5:
		season = "Northern Spring"
	elif month_number < 12.5:
		season = "Northern Summer"
	elif month_number < 17.3:
		season = "Northern Fall"
	else:
		season = "Northern Winter"
	print "It's a beautiful", season, "day."

	
def end_transmission():
	time.sleep(2)
	print "I'm so lonely."
	time.sleep(1)
	sleeper()
	sleeper()
	print "[End Transmission]"	
	time.sleep(2)


if __name__ == "__main__":
	print " "
	
	curiosity()	
	Thread(target=coldest_temp).start()
	Thread(target=warmest_temp).start()
	season_calculator(month)

	weather_report(low_temp,high_temp,conditions)

	sunset_mars(sunset)	
	
	current_time()
	sunset_time()

	
	








