# Authors:                                Sandro Aguilar
# Date:                                   April 17, 2021
# Class:                                  CS 361
# Description:                            This module holds the index page for the web app
#                                         and is a separate blueprint module.
#

#-------------------------------------------------------------------------
# import the required libraries for the web app and other modules
from flask import redirect, url_for, request, render_template, Blueprint
from mod_index.cryptoData import get_crypto_data
from mod_index.cryptoProcessData import clean_data

# create a blueprint module
index_bp = Blueprint('index_bp', __name__, template_folder='templates')

# blueprint routes
@index_bp.route('/', methods=['GET'])
def index():
  home = 'active'
  json_crypto_data = get_crypto_data()
  data = clean_data(json_crypto_data)
  print(data)

  return render_template('home.html', home_menu=home)