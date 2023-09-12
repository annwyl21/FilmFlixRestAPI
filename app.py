# TUTORIAL LINK https://levelup.gitconnected.com/full-stack-web-app-with-python-react-and-bootstrap-backend-8592baa6e4eb

from flask import Flask, request, jsonify
import requests
from show_all_records import get_films_as_dict
from flask_cors import CORS
import sqlite3 as sql # sql lite module
# create the Flask app and configure the app to allows access to our endpoints from any ip-address using CORS


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

if __name__ == '__main__':
	app.debug = True
	app.run(debug=True)
	app.run()