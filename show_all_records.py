

# # db con is a variable that is initialised with everything on the right
# dbcon = sql.connect("filmflix.db") # connect method create new or use an existing db

# # assign cursor method to dbCursor to allow us to execute/ run sql queries and statements
# dbCursor = dbcon.cursor()

def get_films_as_dict():

	film_collection = []

	#dbcon.row_factory = sql.Row
	dbCursor.execute('SELECT * FROM tblfilms')
	rows = dbCursor.fetchall()
	#print(rows)

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
	
	return film_collection


if __name__ == '__main__':
	print(get_films_as_dict())

# filmID(integer), title(text), yearReleased(integer),rating(text),duration(integer),genre(text) 
