# Authors:                                Sandro Aguilar
# Date:                                   April 20, 2021
# Class:                                  CS 361
# Description:                            This file contains helper functions to
#                                         implement the Wikiscraper.

#-------------------------------------------------------------------------
# import the required libraries for the web app and other modules
from bs4 import BeautifulSoup
import requests


# implement function that returns links
#-------------------------------------------------------------------------
def get_links(url, get_pdfs = False):
  r = requests.get(url)

  content = r.content

  soup = BeautifulSoup(content, 'html.parser')

  links = soup.find_all('a', href=True)

  # list to hold PDF links
  link_list = []

  # search for PDF links and save thim in a list
  for link in links:
    current_link = link.get('href')

    if get_pdfs:
      # get pdf links if option selected
      if current_link.endswith('pdf'):
        link_list.append(link['href'])
      else:
        continue
    else:
      # get all links if option is not selected
      link_list.append(link['href'])

  return link_list