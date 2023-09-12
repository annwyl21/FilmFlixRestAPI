from connect import *

def get_films():
	dbCursor.execute('SELECT * FROM tblfilms')

	all_records = dbCursor.fetchall()

	for each_record in all_records:
		print(each_record)

if __name__ == '__main__':
	get_films()
