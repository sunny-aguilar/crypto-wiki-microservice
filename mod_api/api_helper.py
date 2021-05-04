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
  # print('URL:', url)        # test to see if URL was received
  URL = url
  r = requests.get(URL)

  content = r.content

  soup = BeautifulSoup(content, 'html.parser')

  # ref = soup.find("a")
  links = soup.find_all('a', href=True)

  pdf_links = [];

  for link in links:
    print(link['href'][-3:])
    print(link['href'])
    if link['href'][-3:] == '.pdf':
      print(link['href'])
      pdf_links.append(link['href'])