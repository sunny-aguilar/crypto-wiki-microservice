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
# Start Web App
if __name__ == "__main__":
    app.run(host='localhost', port=55055, debug=True)