import requests

def fetchAPOD():
  URL_APOD = "https://api.nasa.gov/planetary/apod"
  params = {
      'api_key':'0U7D9wfke1uQ0leQL4gOYVIN3PDJqyTeMxAI5DxS',
      'hd':'True'
  }
  response = requests.get(URL_APOD,params=params).json()
  return response

fetchAPOD()