# Authors:                                Sandro Aguilar
# Date:                                   April 18, 2021
# Class:                                  CS 361
# Description:                            This module holds the GUI page for the web app
#                                         and is a separate blueprint module.
#

#-------------------------------------------------------------------------
# import the required libraries for the web app and other modules
from flask import redirect, url_for, request, render_template, Blueprint

# create a blueprint module
gui_bp = Blueprint('gui_bp', __name__, template_folder='templates')

# blueprint routes
@gui_bp.route('/gui', methods=['GET'])
def gui():
  return render_template('gui.html')