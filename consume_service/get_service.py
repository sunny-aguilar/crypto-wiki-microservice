# Authors:                                Sandro Aguilar
# Date:                                   May 21, 2021
# Class:                                  CS 361
# Description:                            This module consumes the BTC converter service from my
#                                         group member Garrett B. His API requires a GET request
#                                         and a JSON response is received that returns the prices
#                                         of crypto assets requested.

#-------------------------------------------------------------------------
# import the required libraries for the web app and other modules
from requests import Request
import requests, json

def get_prices(coins):
  # base URL
  base_url = 'https://triviabot-converter.herokuapp.com/convert?'

  # make GET request to microservice
  r = requests.get(base_url+coins)

  # parse server response
  response = ''
  if r.status_code == 200:
    response = r.text
  else:
    response = 'server unresponsive'

  # return server response
  return json.loads(response)
