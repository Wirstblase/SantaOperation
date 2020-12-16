#%load_ext autotime
'''import pandas as pd
import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import matplotlib.pyplot as plt
import plotly_express as px
import tqdm
from tqdm.notebook import tqdm_notebook'''
'''
locator = Nominatim(user_agent="myGeocoder")
coordinates = "53.480837, -2.244914"
location = locator.reverse(coordinates)
print(location.raw)'''

from faker import Faker
fake = Faker()

def randomCoords(): #1/498314639164189341 success rate to be a real location , NEEDS CONSTRAINTS!!
    y = fake.longitude()
    x = fake.latitude()
    while(x<-90 or x>90):
        x = fake.latitude()
    #print(x)
        
    #x-lat, y-lon
    coord = [str(x),str(y)]
    return coord

def randomfakelocation():
    city = fake.city()
    country = fake.country()
    housenumber = fake.building_number()
    street = fake.street_name() 
    shortloc = "I live in " + city + " , " + country
    longloc = street + " , " + housenumber + " , " + city + " , " + country
    location = [shortloc, longloc]
    return location

import random

def randomlocprefix():
    rlparray = ["I live in","I'm from","I am from","I come from","I live at"]
    i = random.randint(0, len(rlparray)-1)
    #print(i)
    rlp = rlparray[i]
    return rlp

def randomlocation():
    print("-generating location-")
    
    coord = randomCoords()
    i = 0
    while(i == 0):
        try:
            coord = randomCoords()
            loc = reversegeocode(coord[1],coord[0])
            housenumber = loc['housenumber']
            street = loc['street']
            city = loc['city']
            i = 1
        except:
            i = 0
    #coord = randomCoords()
    #loc = reversegeocode(coord[1],coord[0])
        
    #location = ["I live in: partial location","full location"] #partial, full
    #location = ["I live in: " + loc.address,str(loc)]
    shortloc = randomlocprefix() + city + " , " + loc['country']
    longloc = street + " , " + housenumber + " , " + city + " , " + loc['country']
    location = [shortloc , longloc]
    
    #location = loc.raw
    return location
    #print(loc)

'''def reversegeocode(latlon):
    #import geopy
    #from geopy.geocoders import Nominatim
    locator = Nominatim(user_agent="myGeocoder")
    location = locator.reverse(latlon)
    return location
'''

import json
import urllib
import requests

def reversegeocode(lat,lon):
    url = 'http://localhost:2322/reverse?lon='+ lon +'&lat=' + lat + '&lang=en'

    data = json.loads(requests.get(url).content.decode('utf-8')) # Here you have the data that you need

    #print(data['features'][0]['properties'])
    return data['features'][0]['properties']


#print(randomlocation())






