#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import sys

#url = 'http://www.usclimatedata.com/climate/los-alamos/new-mexico/united-states/usnm0179'
base = 'http://www.usclimatedata.com/climate'
url = sys.argv[1]
page = requests.get(url)
html = page.content
soup = BeautifulSoup(html, 'html.parser')

#print(soup.find(class_="daily_climate_table"))
html_data = soup.find(class_="daily_climate_table")

headers = html_data.select('th')

weather_data = html_data.select('td')

for i in range(len(headers)): 
    if(i != len(headers) -1):
        print('"' + headers[i].get_text() + '"', end=',')
    else:
        print('"' + headers[i].get_text() + '"')

for i in range(int(len(weather_data)/len(headers))):
    for j in range(len(headers)):
        if(j != len(headers) -1):
            print('"' + weather_data[i*len(headers) + j].get_text()+ '"' , end=',')
        else:
            print('"' + weather_data[i*len(headers) + j].get_text()+ '"')
