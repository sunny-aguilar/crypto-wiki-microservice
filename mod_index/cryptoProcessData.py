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

  id = [1, 1027, 2, 4943(dai), 1975(link), 7083(uni), 825(tether), 3890(poly), 1839(bnb)]

  # get marketcap
  print(data['data'][0]['circulating_supply'])

  # get price
  print(data['data'][0]['circulating_supply'])

  # get circulating supply
  print(data['data'][0]['circulating_supply'])



  return data