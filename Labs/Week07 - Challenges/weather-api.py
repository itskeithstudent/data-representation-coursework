import requests
from bs4 import BeautifulSoup
import csv

'''
Using pretty rudimentary met.ie api
returns response as xml so will use beautifulsoup to parse

Two kinds of get requests can be sent, a current forecast, which is done below.
And a specified to and from forecast, which I may implement if I've time, could be interesting to have it pull last weeks worth of forecast
https://data.gov.ie/dataset/met-eireann-weather-forecast-api
'''

#using latitude and longitude for Athlone due co its centrality and my own bias living there
#interestingly long and latitude results in xml seem to be nearest one
url = 'http://metwdb-openaccess.ichec.ie/metno-wdb2ts/locationforecast?lat=53.423933;long=-7.940690'

response = requests.get(url)
# print(response)
# print(response.text)

#write to file to see what response looks like (commented out for when not testing)
with open("weatherresponse.xml", "w") as newFile:
    newFile.write(response.text)

#use soup to understand the content of response, note: response.content is byte data, response.text is textual, hence why above we use text when writing to file
soup = BeautifulSoup(response.content, 'xml')

#time appears to be the main element of interest
listings = soup.findAll("time")
listings_data = []
listings_columns = ["time", "temp", "temp_unit", "wind_speed", "wind_speed_unit", "humidity", "humidity_unit", "altitude", "longitude", "latitude" ]

for listing in listings:
    'print(listing)'
    #print(listing)
    temp = listing.temperature #['value']
    #print("T"+ temp)

    #if temp is none that means we are getting some precipitation information which we don't want now so continue looping but skip rest of this loop
    if temp == None:
        continue

    time = listing['from']
    temp = listing.temperature['value']
    temp_unit = listing.temperature['unit']
    wind_speed_unit = 'mps'
    wind_speed = listing.windSpeed[wind_speed_unit]
    humidity = listing.humidity['value']
    humidity_unit = listing.humidity['unit']
    altitude = listing.location['altitude']
    longitude = listing.location['longitude']
    latitude = listing.location['latitude']

    listings_data.append([time, temp, temp_unit, wind_speed, wind_speed_unit, humidity, humidity_unit, altitude, longitude, latitude ])
    print(time,temp,wind_speed,humidity)
    #break

with open('athlone_weather.csv', mode='w', newline='') as weather_csv:
    weather_writer = csv.writer(weather_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    weather_writer.writerow(listings_columns)
    weather_writer.writerows(listings_data)