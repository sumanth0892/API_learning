#Connecting to a database
#The database used in SQLite, a lightweight database engine that is supported in Python.

import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config['DEBUG'] = True

def dict_factory(cursor,row):
	d = {}
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d

@app.route('/',methods = ['GET'])
def home():
	return 'Distant Reading Archive'

@app.route('/api/v1/resources/books/all',methods = ['GET'])
def api_all():
	conn = sqlite3.connect('books.db') #Connect to the database using the sqlite3 library.
	conn.row_factory = dict_factory #Use the dict_factory function we've created which returns the items as dictionaries than lists.
	cur = conn.cursor() #A cursor object which actually moves through the database.
	all_books = cur.execute('SELECT * FROM books;').fetchall() #Asks the cursor to execute this query which pulls in all the data
	return jsonify(all_books) #Return this information as a json.

@app.errorhandler(404)
def page_not_found(e):
	#Create an error page seen by the user if the user encounters an error or inputs a route that hasn't been defined.
	return 'The resource could not be found'

@app.route('/api/v1/resources/books',methods = ['GET'])
def api_filter():
	#Improvement on the api_id() function and allows to filter by more parameters such as id, published and author.
	query_parameters = request.args #Pulls the supported parameters id, published and author
	id = query_parameters.get('id') #Bind to id
	published = query_parameters.get('published') #Bind to published
	author = query_parameters.get('author') #Bind to author.

	#The next segment builds the SQL query
	query = "SELECT * FROM books WHERE"
	to_filter = []

	if id:
		query += ' id=? AND'
		to_filter.append(id)
	if published:
		query += ' published=? AND'
		to_filter.append(published)
	if author:
		query += ' author=? AND'
		to_filter.append(author)
	if not (id or published or author):
		return page_not_found(404)
	#Remove the trailing 'AND' and add the semi-colon required for SQL queries.
	query = query[:-4] + ';'

	conn = sqlite3.connect('books.db')
	conn.row_factory = dict_factory
	cur = conn.cursor()
	results = cur.execute(query, to_filter).fetchall()
	return jsonify(results)

app.run()

