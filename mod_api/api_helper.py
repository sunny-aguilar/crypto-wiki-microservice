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

  # list to hold PDF links
  pdf_links = [];

  # search for PDF links and save thim in a list
  for link in links:
    current_link = link.get('href')
    if current_link.endswith('pdf'):
      pdf_links.append(link['href'])

  # print(pdf_links)
  # return pdf links
  return pdf_links