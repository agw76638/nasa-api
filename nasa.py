import requests
from bs4 import BeautifulSoup

def fetchAPOD():
  URL_APOD = "https://api.nasa.gov/planetary/apod"
  #date = '2020-01-22'
  params = {
      'api_key':'0U7D9wfke1uQ0leQL4gOYVIN3PDJqyTeMxAI5DxS',
      #'date':date,
      'hd':'True'
  }
  response = requests.get(URL_APOD,params=params).json()
  print(response)
  return response
  #soup = BeautifulSoup(response.text, "html.parser")
fetchAPOD()