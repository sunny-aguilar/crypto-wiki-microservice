# Authors:                                Sandro Aguilar
# Date:                                   April 20, 2021
# Class:                                  CS 361
# Description:                            This module holds the api endpoint for the web app
#                                         and is a separate blueprint module.
#

#-------------------------------------------------------------------------
# import the required libraries for the web app and other modules
from flask import redirect, url_for, request, render_template, Blueprint, jsonify
import wikipediaapi

# create a blueprint module
api_bp = Blueprint('api_bp', __name__, template_folder='templates')

# blueprint routes
@api_bp.route('/api', methods=['GET'])
def api():
  if request.method == 'GET':
    print('API end-point accessed------------------------------')

    # get parameters
    print(request.form)
    req = request.args
    search_term = req.get('search_term')
    url = req.get('url')
    title = req.get('title')
    summary = req.get('summary')
    sections = req.get('sections')
    text = req.get('text')
    links = req.get('links')
    print(f'Search term: {search_term}')
    print(f'URL: {url}')
    print(f'Title: {title}')
    print(f'Summary: {summary}')
    print(f'Sections: {sections}')
    print(f'Text: {text}')
    print(f'Links: {links}')

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
      print(page.summary)
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
      # print_links(page)

      if links:
        page_data['links'] = print_links(page.links)
        print(page_data)

    books = [
      {'id': 0,
        'title': 'A Fire Upon the Deep',
        'author': 'Vernor Vinge',
        'first_sentence': 'The coldsleep itself was dreamless.',
        'year_published': '1992'},
      {'id': 1,
        'title': 'The Ones Who Walk Away From Omelas',
        'author': 'Ursula K. Le Guin',
        'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
        'published': '1973'},
      {'id': 2,
        'title': 'Dhalgren',
        'author': 'Samuel R. Delany',
        'first_sentence': 'to wound the autumnal city.',
        'published': '1975'}
    ]

  return jsonify(books)
  # return render_template('gui.html', msg=msg)
