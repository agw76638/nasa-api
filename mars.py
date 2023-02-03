import requests
from flask import request
from flask_sqlalchemy import SQLAlchemy

def fetchMARS():
  URL_MARS = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos"
  params = {
      'api_key':'0U7D9wfke1uQ0leQL4gOYVIN3PDJqyTeMxAI5DxS'
  }
  response = requests.get(URL_MARS,params=params).json()
#   page = request.args.get('page', 1, type=int)
  images = []
  for image in images:
    image_data = {
        'url': response['latest_photos'][0]['img_src']
    }
#   posts = response.paginate(page=page, per_page=2)
  print(response['latest_photos'][0]['img_src'])

  return response

fetchMARS()