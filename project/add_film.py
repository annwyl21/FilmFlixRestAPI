from connect import *
import user_data_validation

def get_data():
	title = user_data_validation.get_title()
	year_released = user_data_validation.get_release_year()
	rating = user_data_validation.get_rating()
	duration = user_data_validation.get_duration()
	genre = user_data_validation.get_genre()
	return title, year_released, rating, duration, genre

def insert_film():
	data_tuple = get_data()
	title, year_released, rating, duration, genre = data_tuple

	dbCursor.execute("INSERT INTO tblfilms(title, yearReleased, rating, duration, genre) VALUES(?, ?, ?, ?, ?)", (title, year_released, rating, duration, genre))

	dbcon.commit()
	print(f"{title} inserted")
