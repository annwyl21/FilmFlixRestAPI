from connect import *

def get_title():
	title = input("Enter Film Title:\n").title()
	return title

def get_release_year():
	year_released = int(input("Enter Year of Release\n"))
	return year_released

def get_rating():
	rating = input("Enter MPA Film Rating\n").upper()
	return rating

def get_duration():
	duration = int(input("Enter Film Duration\n"))
	return duration

def get_genre():
	# retrieve genres available
	dbCursor.execute(f"SELECT distinct(genre) FROM tblfilms order by genre asc")
	tuple_rows = dbCursor.fetchall()

	print('Film Flix Database has movies of the following Genre...')
	for num, row in enumerate(tuple_rows, 1):
		print(f"{num:2d} {row[0]}")
	user_input = int(input('Enter number:\n'))
	
	for num, row in enumerate(tuple_rows, 1):
		if user_input == num:
			genre = row[0]

	#genre = input("Enter Film Genre\n").title()
	return genre

if __name__ == '__main__':
	print(get_genre())