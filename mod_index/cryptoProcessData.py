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

  # save coin data in array that will hold objects of coin data
  coin_data = []

  # CMC coin IDs
  id = [1, 1027, 2, 4943, 1975, 7083, 825, 3890, 7186, 1839]

  # get coin data from data
  # print('ID FOUND:', data['data'][0]['id'])
  # print('Market Cap:', data['data'][0]['quote']['USD']['market_cap'])
  # print('Circulating Supply:', data['data'][0]['circulating_supply'])

  # find coin data by iterating in data
  for coin in data['data']:
    # get Bitcoin data
    if coin['id'] is 1:
      coin_specs = {}
      coin_specs["name"] = coin['name']
      coin_specs["market_cap"] = coin['quote']['USD']['market_cap'];
      coin_specs["circulating_supply"] = coin['circulating_supply'];
      coin_data.append(coin_specs)

    # get Ether data
    if coin['id'] is 1027:
      coin_specs = {}
      coin_specs["name"] = coin['name']
      coin_specs["market_cap"] = coin['quote']['USD']['market_cap'];
      coin_specs["circulating_supply"] = coin['circulating_supply'];
      coin_data.append(coin_specs)
  print(coin_data)
    # get Litecoin data
    # get Dai data
    # get USDT data
    # get Link data
    # get Uniswap data
    # get Polygon data
    # get Cake data
    # get BNB data




  return data