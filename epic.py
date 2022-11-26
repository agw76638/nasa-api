import requests

def fetchEPIC():
  URL_EPIC = "https://api.nasa.gov/EPIC/api/natural/"
  params = {
      'api_key':'0U7D9wfke1uQ0leQL4gOYVIN3PDJqyTeMxAI5DxS'
  }
  response = requests.get(URL_EPIC,params=params).json()

  return response
  print(response)

fetchEPIC()