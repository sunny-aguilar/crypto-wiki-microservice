# Authors:                                Sandro Aguilar
# Date:                                   April 5, 2021
# Class:                                  CS 361
# Description:                            Pproject that implements a microservices strategy with
#                                         my other team members. The main project consists of
#
#
# The software you write will need
#                                         to communicate (request data, receive data, receive
#                                         requests, and send data) with software your teammates
#                                         write.

#-------------------------------------------------------------------------
from mod_index.index import index
from flask import Flask, render_template

# import blueprints
from mod_index.index import index_bp
from mod_gui.gui import gui_bp
from mod_api.api import api_bp
from mod_docs.docs import docs_bp


#-------------------------------------------------------------------------
# create the flask app & set app configurations
app = Flask(__name__, static_url_path='/static')


#-------------------------------------------------------------------------
# register blueprint modules
app.register_blueprint(index_bp)
app.register_blueprint(gui_bp)
app.register_blueprint(api_bp)
app.register_blueprint(docs_bp)


#-------------------------------------------------------------------------
# routes in blueprints



# route errors -----
@app.errorhandler(404)
def page_not_found(error):
  msg = "Oh snap, the page you requested was not found"
  return render_template('not_found.html', results=msg), 404

@app.errorhandler(500)
def server_error(error):
  msg = "Oh snap, it looks like the programmers made a boo boo. Go to the main page to clear this up."
  return render_template('server_error.html', results=msg), 500




#-------------------------------------------------------------------------
# Start Web App
if __name__ == "__main__":
    app.run(host='localhost', port=55056, debug=True)

# OSU - run from osu servers using gunicorn
# gunicorn -b 0.0.0.0:55055 -D app:app