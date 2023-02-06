import requests
import random
from flask import request

def fetchMars(url):
  response = requests.get(url).json()
  latest_photos = response['latest_photos']
  length = len(latest_photos) - 1
  number = random.randint(0, length)
  src = latest_photos[number]['img_src']
  date = latest_photos[number]['earth_date']
  sol = latest_photos[number]['sol']

  return {'src': src, 'date': date,'sol': sol}

# def marsData(url):
#   URL = url
#   response = requests.get(url).json()
#   latest_photos = response['latest_photos']
#   length = len(latest_photos)-1
#   datas = []
#   for i in range(4):
#     data = fetchMars(URL, i)
#     print(data, i)
#     datas.append(data)
#     i = i+1
#   print(datas)
#   return datas

def getMars():
  URL_MARS = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?api_key=0U7D9wfke1uQ0leQL4gOYVIN3PDJqyTeMxAI5DxS"
  datas = fetchMars(URL_MARS)
  return datas

getMars()