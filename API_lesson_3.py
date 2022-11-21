#Finding specific resources API
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config['DEBUG'] = True

#Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/',methods = ['GET'])
def home():
	return "Distant reading archive"

#A route to return all of the available entries
@app.route('/api/v1/resources/books/all',methods = ['GET'])
def api_all():
	#At the specific sub-URl 'api/v1/resources/books/all' we (users) get the books dictionary as a json dictionary.
 	return jsonify(books)


@app.route('/api/v1/resources/books',methods = ['GET'])
def app_id():
 # Check if an ID was provided as part of the URL.
 # If ID is provided, assign it to a variable.
 # If no ID is provided, display an error in the browser.
 	if 'id' in request.args:
 		id = int(request.args['id'])
 	else:
 		return "Error: No field ID provided."
 	#Create an empty list for the results.
 	results = []
 	for book in books:
 		if id == book['id']:
 			results.append(book)
 	return jsonify(results)

app.run()