# Authors:                                Sandro Aguilar
# Date:                                   April 20, 2021
# Class:                                  CS 361
# Description:                            This file contains helper functions to
#                                         implement the Wikiscraper.

#-------------------------------------------------------------------------
# import the required libraries for the web app and other modules
from bs4 import BeautifulSoup
import requests

# implement function
#-------------------------------------------------------------------------
def pdf_links(url):
  print('URL:', url)
  URL = url
  r = requests.get(URL)

  content = r.content

  print(content)
  # soup = BeautifulSoup(content)