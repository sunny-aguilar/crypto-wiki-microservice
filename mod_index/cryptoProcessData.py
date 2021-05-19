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
  # coin_data = []
  coin_data = {}

  # CMC coin IDs
  asset_id = [1, 1027, 2, 4943, 825, 1975, 7083, 3890, 7186, 1839]

  # find coin data by iterating in data
  for coin in data['data']:
    # push coin data into object and append to coin_data object
    for asset in asset_id:
      if coin['id'] == asset:
        coin_specs = {}
        coin_specs['name'] = coin['name']
        coin_specs['id'] = coin['id']
        coin_specs['market_cap'] = format(int(coin['quote']['USD']['market_cap']), ',')
        coin_specs['circulating_supply'] = format(int(coin['circulating_supply']), ',')
        # coin_specs['max_supply'] = format(int(coin['max_supply']), ',')
        coin_specs['max_supply'] = format(int(coin['max_supply']), ',') if coin['max_supply'] != None else "Unlimited"
        coin_data[coin['name']] = (coin_specs)

  return coin_data