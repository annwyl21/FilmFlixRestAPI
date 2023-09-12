from connect import *
import user_data_validation

def select_genre():
	genre = user_data_validation.get_genre()

	dbCursor.execute(f"SELECT * FROM tblfilms where genre = '{genre}'")

	all_records = dbCursor.fetchall()

	for each_record in all_records:
		print(each_record)

if __name__ == '__main__':
	select_genre()