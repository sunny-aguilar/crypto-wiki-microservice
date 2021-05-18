# Authors:                                Sandro Aguilar
# Date:                                   May 8, 2021
# Class:                                  CS 361
# Description:                            This module connects to CoinMarketCap
#                                         to obtain data on crypto assets.
#

#-------------------------------------------------------------------------
# import the required libraries for the web app and other modules
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


def get_crypto_data():
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  parameters = {
    # 'symbol':'BTC,ETH',
    # 'limit':'10',
    # 'convert':'USD'
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '8fa33cd2-e221-4b18-81f5-58344e93b3e7',
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    print(data)
    return data
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    return e