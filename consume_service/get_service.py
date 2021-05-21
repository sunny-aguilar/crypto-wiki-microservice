# Authors:                                Sandro Aguilar
# Date:                                   May 21, 2021
# Class:                                  CS 361
# Description:                            This module consumes the BTC converter service from my
#                                         group member Garrett B. His API requires a GET request
#                                         and a JSON response is received that returns the prices
#                                         of crypto assets.

#-------------------------------------------------------------------------
# import the required libraries for the web app and other modules
from requests import Request
import requests

def get_prices():
  base_url = 'https://triviabot-converter.herokuapp.com/convert?'
  param_1 = 'crypto1=BTC&curr1=USD&crypto2=ETH&curr2=USD&crypto3=ltc&curr3=USD&crypto4=dai&curr4=USD&crypto5=usdt&curr5=USD'
  param_2 = 'crypto1=BTC&curr1=USD&crypto2=ETH&curr2=USD&crypto3=ltc&curr3=USD&crypto4=dai&curr4=USD&crypto5=usdt&curr5=USD'

  # make GET request to microservice
  r = requests.get(base_url+param_1)
  print('Status code:',r.status_code)

  return 0
