# Authors:                                Sandro Aguilar
# Date:                                   April 20, 2021
# Class:                                  CS 361
# Description:                            This module holds the api endpoint for the web app
#                                         and is a separate blueprint module. This API
#                                         end-point is to access a Wikipedia webscraper.
# Base URL:                               http://localhost:55055/api

#-------------------------------------------------------------------------
# import the required libraries for the web app and other modules
from flask import redirect, url_for, request, render_template, Blueprint, jsonify
from mod_api.api_helper import pdf_links
import wikipediaapi


# create a blueprint module
api_bp = Blueprint('api_bp', __name__, template_folder='templates')

# blueprint routes
@api_bp.route('/api', methods=['GET'])
def api():
  if request.method == 'GET':
    print('API end-point accessed------------------------------')

    # get parameters
    req = request.args
    search_term = req.get('search_term')
    # handle empty search_term
    if search_term is '':
      msg = 'Enter a search term.'
      return render_template('gui.html', msg=msg)

    url = req.get('url')
    title = req.get('title')
    summary = req.get('summary')
    sections = req.get('sections')
    text = req.get('text')
    links = req.get('links')
    # pdf_links = req.get('pdf_links')

    # warn user that they must select at least one parameter
    if all(params is None for params in (url, title, summary, sections, text, links)):
      msg = 'Select at least one search parameters.'
      return render_template('gui.html', msg=msg)


    # set up wikipedia search API
    wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
    )


    # scrape page and save in object
    page = wiki_wiki.page(search_term)


    # check if page exists to continue with web scraper
    if (page.exists()):
      print('PAGE EXISTS!')
      print('Page Exists: %s' % page.exists())
      print(page.fullurl)
      print(page.title)
      # print(page.summary)
      # print(page.text)


      # create dictionary to store page data
      page_data = {}

      # store data in dictionary
      if url:
        page_data['url'] = page.fullurl

      if title:
        page_data['title'] = page.title

      if summary:
        page_data['summary'] = page.summary

      # get page sections
      def get_sections(sections):
        section_arr = []
        for s in sections:
          section_arr.append(s.title)
        return section_arr

      if sections:
        page_data['sections'] = get_sections(page.sections)

      # get page text
      if text:
        page_data['text'] = page.text
        print(page_data)

      # get links to other pages
      def print_links(links):
        link_arr = []
        for title in sorted(links.keys()):
          print("%s" % (title))
          link_arr.append(title)
        return link_arr

      if links:
        page_data['links'] = print_links(page.links)
        print(page_data)

      if pdf_links:
        # if PDF links are requested, call helper function
        page_data['pdf_links'] = pdf_links(page.fullurl)


      # return scraper data via JSON notation
      return jsonify(page_data)

  # if page does not exist, return an empty JSON object
  return jsonify({})