import flask
app = flask.Flask(__name__) #Creates the Flask application object which contains the data about the application and the methods that tell the application to do things.
app.config['DEBUG'] = True #Starts the debugger

@app.route('/',methods = ['GET'])
def home():
	return 'Home'

app.run() #Method that runs the application server.