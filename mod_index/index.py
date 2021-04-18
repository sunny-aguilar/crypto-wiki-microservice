# Authors:                                Sandro Aguilar
# Date:                                   April 17, 2021
# Class:                                  CS 361
# Description:                            This module holds the index page for the web app
#                                         and is a separate blueprint module.
#

#-------------------------------------------------------------------------
# import the required libraries for the web app and other modules
from flask import redirect, url_for, request, render_template, Blueprint

# create a blueprint module
index_bp = Blueprint('index_bp', __name__)

# blueprint routes
index_bp.route('/', methods=['GET'])

