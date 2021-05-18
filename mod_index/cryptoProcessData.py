# Authors:                                Sandro Aguilar
# Date:                                   May 9, 2021
# Class:                                  CS 361
# Description:                            This module processes the data obtained
#                                         from the CMC api to obtain the following
#                                         data:
#                                         - coin names
#                                         - symbols
#                                         - total supply
#

#-------------------------------------------------------------------------
# import the required libraries for the web app and other modules


def clean_data(raw_data):
  data = raw_data

  # CMC coin IDs
  id = [1, 1027, 2, 4943, 1975, 7083, 825, 3890, 7186, 1839]

  # get marketcap
  print(data['data'][0]['id'])
  print(data['data'][0]['quote']['USD']['market_cap'])
  print(data['data'][0]['circulating_supply'])

  for coin in data['data']:
    if coin['id'] is 1:
      print('ID FOUND:', coin['id'])
      print(coin['id']['USD']['market_cap'])
      print(coin['id']['circulating_supply'])


  # get price
  print(data['data'][0]['circulating_supply'])

  # get circulating supply
  print(data['data'][0]['circulating_supply'])



  return data