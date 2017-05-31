import csv
import urllib
import json
import time

url = "https://maps.googleapis.com/maps/api/geocode/json?address="
key = ",+los+alamos,+NM&key=AIzaSyDIhPAbuC4ln0iVgTiUDQpXuTtKUlMDuLk"

lookup = {}
bad = {}
 
count =  1
calls = 1

with open("2017-03-28_Meter_Street.csv","rb") as tmpcsv:
	csvreader = csv.reader(tmpcsv,delimiter=',')
	next(csvreader)

	for row in csvreader:
		cust_id = row[2]
		street = row[3]
		
		street = street[:-2]
		street = street[2:]
		street = street.replace(" ", "+")
		#count = count + 1
		#calls = calls + 1
		construct = url + street + key
		call = urllib.urlopen(construct)
		
		data = json.load(call)
		if data['status'] == 'ZERO_RESULTS':
			print("Cust " + str(cust_id) + "invalid result")
			bad[cust_id] = data['status']
		else:
			lat_long = data['results'][0]['geometry']['location']
			print(cust_id)
			lookup[cust_id]=lat_long
		time.sleep(0.1)

with open("lat_long.csv","wb") as tmpcsv:
	line = "MR_MDVC_NUMBER,Latitude,Longitude\n"
	tmpcsv.write(line)
	for key in lookup.keys():
		idnum = str(key)
		lat = str(lookup[key]['lat'])
		lng = str(lookup[key]['lng'])
		comma = ","
		nl = "\n"
		line = idnum + comma + lat + comma + lng + nl
		tmpcsv.write(line)

with open("bad_address.csv","wb") as tmpcsv:
	line = "MR_MDVC_NUMBER,bad\n"
	tmpcsv.write(line)
	for key in bad.keys():
		comma = ","
		nl ="\n"
		line = str(key) + comma + str(bad[key]) + nl
		tmpcsv.write(line)
