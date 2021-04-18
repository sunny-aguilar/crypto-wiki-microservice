# Authors:                                Sandro Aguilar
# Date:                                   April 5, 2021
# Class:                                  CS 361
# Description:                            Pproject that implements a microservices strategy with
#                                         my other team members. The software you write will need
#                                         to communicate (request data, receive data, receive
#                                         requests, and send data) with software your teammates
#                                         write.

#-------------------------------------------------------------------------
from flask import Flask, render_template



#-------------------------------------------------------------------------
# create the flask app & set app configurations
app = Flask(__name__, static_url_path='/static')



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
    app.run(host='localhost', port=55055, debug=True)