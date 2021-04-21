# Authors:                                Sandro Aguilar
# Date:                                   April 20, 2021
# Class:                                  CS 361
# Description:                            This module holds the api endpoint for the web app
#                                         and is a separate blueprint module.
#

#-------------------------------------------------------------------------
# import the required libraries for the web app and other modules
from flask import redirect, url_for, request, render_template, Blueprint

# create a blueprint module
api_bp = Blueprint('api_bp', __name__, template_folder='templates')

# blueprint routes
@api_bp.route('/api', methods=['GET', 'POST'])
def api():
  if request.method == 'GET':
    print('GET REQUEST RECEIVED')
  elif request.method == 'POST':
    print('POST REQUEST RECEIVED')

  print('API endpoint accessed!')

  msg = 'GUI page.'
  return redirect('/')
  return render_template('/', msg=msg)
  # return render_template('gui.html', msg=msg)
