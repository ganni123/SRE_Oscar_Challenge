# import flask
from flask import Flask

# create an app instance          
app = Flask(__name__) 

# at the end point /
@app.route("/")

# call method hello                  
def hello():

# which returns "hello world"                          
    return "Hello World!"

# on running python flask.py             
if __name__ == "__main__":

# run the flask app            
    app.run()                     