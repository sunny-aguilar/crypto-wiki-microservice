# Authors:                                Sandro Aguilar
# Date:                                   April 22, 2021
# Class:                                  CS 361
# Description:                            This module holds the Docs page for the web app
#                                         and is a separate blueprint module.
#

#-------------------------------------------------------------------------
# import the required libraries for the web app and other modules
from flask import redirect, url_for, request, render_template, Blueprint

# create a blueprint module
docs_bp = Blueprint('gui_docs', __name__, template_folder='templates')

# blueprint routes
@docs_bp.route('/docs', methods=['GET'])
def gui():
  docs = 'active'
  return render_template('docs.html', docs_menu=docs)

