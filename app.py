# TUTORIAL LINK https://levelup.gitconnected.com/full-stack-web-app-with-python-react-and-bootstrap-backend-8592baa6e4eb

from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3 as sql # sql lite module
# create the Flask app and configure the app to allows access to our endpoints from any ip-address using CORS
# https://flask-cors.readthedocs.io/en/latest/
import logging
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "log_CRUD.log", level=logging.critical, format = LOG_FORMAT)
logger = logging.getLogger()

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
		data = request.json
		title = data.get('title')
		year_released = data.get('year_released')
		rating = data.get('rating')
		duration = data.get('duration')
		genre = data.get('genre')
		film_data = {'title': title, 'year_released': year_released, 'rating': rating, 'duration': duration, 'genre': genre}
		
		dbcon = sql.connect("filmflix.db")
		dbCursor = dbcon.cursor()
		dbCursor.execute("INSERT INTO tblfilms(title, yearReleased, rating, duration, genre) VALUES(?, ?, ?, ?, ?)", (title, year_released, rating, duration, genre))
		dbcon.commit()

		logger.info(f'Film Added Successfully: Title {title}')
		return jsonify(film_data)

@app.route('/api/remove/<film_id>', methods=['DELETE'])
def api_remove_film(film_id):
	if request.method == 'DELETE':
		dbcon = sql.connect("filmflix.db")
		dbCursor = dbcon.cursor()
		dbCursor.execute(f"DELETE FROM tblfilms where filmID = {film_id}")
		dbcon.commit()
		logger.info(f'Film Deleted Successfully: Film ID {film_id}')
		return jsonify({'removed': film_id})

@app.route('/api/amend', methods=['PATCH'])
def api_amend_film():
	if request.method == 'PATCH':
		data = request.json
		film_id = data.get('film_id')
		fieldname = data.get('fieldname')
		fieldvalue = data.get('fieldvalue')
		update = {'Film ID': film_id, 'Field To Update': fieldname, 'Value': fieldvalue}

		dbcon = sql.connect("filmflix.db")
		dbCursor = dbcon.cursor()
		dbCursor.execute(f"UPDATE tblfilms SET {fieldname} = '{fieldvalue}' WHERE filmId = {film_id}")
		dbcon.commit()
		logger.info(f"Record Updated: {film_id} {fieldname} updated to {fieldvalue}")
		return jsonify(update)

if __name__ == '__main__':
	app.run()