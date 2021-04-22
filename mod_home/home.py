# Authors:                                Sandro Aguilar
# Date:                                   April 18, 2021
# Class:                                  CS 361
# Description:                            This module holds the home page for the web app
#                                         and is a separate blueprint module.
#

#-------------------------------------------------------------------------
# import the required libraries for the web app and other modules
from flask import redirect, url_for, request, render_template, Blueprint

# create a blueprint module
home_bp = Blueprint('home_bp', __name__, template_folder='templates')

# blueprint routes
@home_bp.route('/gui', methods=['GET'])
def gui():
  gui = 'active'
  return render_template('gui.html', gui_menu=gui)