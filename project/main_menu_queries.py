from connect import *

# dynamic count of movies available displayed on main menu
def get_database_length():
	
	dbCursor.execute(f"SELECT count(title) as 'Number of Films' FROM tblfilms")

	number_films = dbCursor.fetchone()

	return number_films[0]

# dynamic sum of minutes in database, converted to hours and displayed on main menu
def get_film_hours():
	dbCursor.execute(f"SELECT sum(duration) as 'Minutes' FROM tblfilms")

	minutes = dbCursor.fetchone()

	return minutes[0]
	

if __name__ == '__main__':
	print(get_database_length())
	print(get_film_hours())
	