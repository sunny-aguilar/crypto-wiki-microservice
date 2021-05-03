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
def get_pdf_links():
  URL = "http://www.values.com/inspirational-quotes"
  r = requests.get(URL)