# TUTORIAL LINK https://levelup.gitconnected.com/full-stack-web-app-with-python-react-and-bootstrap-backend-8592baa6e4eb

from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3 as sql # sql lite module
# create the Flask app and configure the app to allows access to our endpoints from any ip-address using CORS
# https://flask-cors.readthedocs.io/en/latest/


app = Flask(__name__)
CORS(app)

@app.route('/api/films', methods=['GET'])
def api_get_films():
	dbcon = sql.connect("filmflix.db")
	dbCursor = dbcon.cursor()
	dbCursor.execute('SELECT * FROM tblfilms')
	rows = dbCursor.fetchall()
		
	film_collection = []
	# convert row objects to dictionary
	for film_data_tuple in rows:
		#print(film_data_tuple)
		film = {}
		film['id'] = film_data_tuple[0]
		film['title'] = film_data_tuple[1]
		film['year_released'] = film_data_tuple[2]
		film['rating'] = film_data_tuple[3]
		film['duration'] = film_data_tuple[4]
		film['genre'] = film_data_tuple[5]
		film_collection.append(film)
	
	return jsonify(film_collection)

@app.route('/api/add', methods=['POST'])
def api_add_film():
	if request.method == 'POST':
		title = request.args.get('title')
		year_released = request.args.get('year_released')
		rating = request.args.get('rating')
		duration = request.args.get('duration')
		genre = request.args.get('genre')
		
		dbcon = sql.connect("filmflix.db")
		dbCursor = dbcon.cursor()
		dbCursor.execute("INSERT INTO tblfilms(title, yearReleased, rating, duration, genre) VALUES(?, ?, ?, ?, ?)", (title, year_released, rating, duration, genre))
		dbcon.commit()
		return jsonify({'test': 'test'})

if __name__ == '__main__':
	app.debug = True
	app.run(debug=True)
	app.run()