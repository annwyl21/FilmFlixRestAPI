# TUTORIAL LINK https://levelup.gitconnected.com/full-stack-web-app-with-python-react-and-bootstrap-backend-8592baa6e4eb

from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

import sqlite3 as sql # sql lite module

from user_data_check import UserDataCheck

import logging
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "log_CRUD.log", level=logging.ERROR, format = LOG_FORMAT)
logger = logging.getLogger()

current_time = datetime.now()
formatted_time = current_time.strftime('%Y-%m-%d %H:%M')

# create the Flask app and configure the app to allows access to our endpoints from any ip-address using CORS
# https://flask-cors.readthedocs.io/en/latest/
app = Flask(__name__)
CORS(app)

DATABASE = "filmflix.db"
#query & commit function to create clean code
def query_db(query, args=(), one=False):
	dbcon = sql.connect(DATABASE)
	dbCursor = dbcon.cursor()
	dbCursor.execute(query, args) # args helps prevent SQLinjection
	results = dbCursor.fetchall() # setting one to True will return only the first result, making single returns easier to handle
	dbCursor.close()
	dbcon.close()
	return (results[0] if results else None) if one else results

def modify_db(statement, args=()):
	dbcon = sql.connect(DATABASE)
	dbCursor = dbcon.cursor()
	dbCursor.execute(statement, args)
	dbcon.commit()
	dbCursor.close()
	dbcon.close()

# globally available genres and ratings lists to help standardisation
available_ratings = []
available_genres = []

@app.route('/api/films', methods=['GET'])
def api_get_films():
	try:
		rows = query_db('SELECT * FROM tblfilms')
					
		film_collection = []
		# convert row objects to dictionary
		for film_data_tuple in rows:
			film = {}
			film['id'] = film_data_tuple[0]
			film['title'] = film_data_tuple[1]
			film['year_released'] = film_data_tuple[2]
			film['rating'] = film_data_tuple[3]
			film['duration'] = film_data_tuple[4]
			film['genre'] = film_data_tuple[5]
			film_collection.append(film)
		
		distinct_genres = query_db('SELECT distinct(genre) FROM tblfilms order by genre asc')
		for genre in distinct_genres:
			if genre[0] not in available_genres:
				available_genres.append(genre[0])

		distinct_ratings = query_db('SELECT distinct(rating) FROM tblfilms')
		for rating in distinct_ratings:
			if rating[0] not in available_ratings:
				available_ratings.append(rating[0])
		
		data = {'film_collection': film_collection, 'distinct_genres': available_genres, 'distinct_ratings': available_ratings}
		
		return jsonify(data)
	
	except sql.DatabaseError as e:
		logger.error("GET FILM FAILED: Database Error")
		return jsonify({'error': 'Database Error'})

@app.route('/api/check', methods=['POST'])
def api_check_film():
	if request.method == 'POST':
		data = request.json
		user_entry = data.get('word')

		title_to_check = UserDataCheck.check_word(user_entry)
		if title_to_check == 'error':
			logger.warning(f"User Input Error: {user_entry}")
			return jsonify({'error': f'Word Invalid, Warning Logged {formatted_time}'})
		
		else:
			try:
				all_records = query_db("SELECT * FROM tblfilms WHERE title LIKE ?", args=('%' + title_to_check + '%',))
			except sql.DatabaseError as e:
				logger.error("CHECK Film FAILED: Database Error")
				return jsonify({'error': 'Database Error'})

			if not all_records:
				logger.info(f'Film Search: Title not found')
				return jsonify({'not found': 'Title not found in database'})
			else:
				for film in all_records:
					logger.info(f'Film Search: Title found')
					return jsonify({'film found': film})

@app.route('/api/add', methods=['POST'])
def api_add_film():
	if request.method == 'POST':
		data = request.json
		
		film_data = UserDataCheck.check_data_to_add(data, available_ratings)
		if 'error' in film_data.values():
			logger.error(f"ADD Film FAILED: Data Entry Error {film_data}")
			return jsonify({'error': 'Data Entry Error'})
		
		else:

			try:
				modify_db("INSERT INTO tblfilms(title, yearReleased, rating, duration, genre) VALUES(?, ?, ?, ?, ?)", (film_data['title'], film_data['year_released'], film_data['rating'], film_data['duration'], film_data['genre']))

				logger.info(f"Film Added Successfully: Title {film_data['title']}")
				return jsonify(film_data)
			
			except sql.DatabaseError as e:
				logger.error("ADD Film FAILED: Database Error")
				return jsonify({'error': 'Database Error'})

@app.route('/api/remove/<user_entry>', methods=['DELETE'])
def api_remove_film(user_entry):
	if request.method == 'DELETE':
		film_id = UserDataCheck.check_film_id(user_entry)
		if film_id == 'error':
			logger.warning(f"User Input Error: {user_entry}")
			return jsonify({'error': f'Film ID {user_entry} invalid, See Warning Log {formatted_time}'})
		
		else:
			film_result = query_db("SELECT * FROM tblfilms WHERE filmID = ?", args=(film_id,))

			if film_result:
				try:
					modify_db("DELETE FROM tblfilms where filmID = ?", args=(film_id,))
					logger.info(f'Film Deleted Successfully: Film ID {film_id}')
					return jsonify({'removed': f"{film_id} {formatted_time}"})
				
				except sql.DatabaseError as e:
					logger.error("DELETE FAILED: Database Error on DELETE attempt")
					return jsonify({'error': f'Database Error, See Error Log {formatted_time}'})
			
			else:
				logger.warning(f"User Input Error: {user_entry}, Failed Attempt to delete film")
				return jsonify({'error': f'Film ID {film_id} invalid, See Warning Log {formatted_time}'})


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
	app.run(debug=True)