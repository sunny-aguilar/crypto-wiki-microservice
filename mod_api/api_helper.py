# Authors:                                Sandro Aguilar
# Date:                                   April 20, 2021
# Class:                                  CS 361
# Description:                            This file contains helper functions to
#                                         implement the Wikiscraper.

#-------------------------------------------------------------------------
# import the required libraries for the web app and other modules
from bs4 import BeautifulSoup
import requests


# implement function that returns pdf links
#-------------------------------------------------------------------------
def pdf_links(url):
  URL = url
  r = requests.get(url)

  content = r.content

  soup = BeautifulSoup(content, 'html.parser')

  # ref = soup.find("a")
  links = soup.find_all('a', href=True)

  # list to hold PDF links
  pdf_links = []

  # search for PDF links and save thim in a list
  for link in links:
    current_link = link.get('href')
    if current_link.endswith('pdf'):
      pdf_links.append(link['href'])

  # print(pdf_links)
  # return pdf links
  return pdf_links


# implement function that returns links
#-------------------------------------------------------------------------
def get_links(url, get_pdfs = False):
  URL = url
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