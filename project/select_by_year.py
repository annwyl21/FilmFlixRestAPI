from connect import *
import user_data_validation

def select_year():
	year = user_data_validation.get_release_year()

	dbCursor.execute(f"SELECT * FROM tblfilms where yearReleased = '{year}'")

	all_records = dbCursor.fetchall()

	for each_record in all_records:
		print(each_record)

if __name__ == '__main__':
	select_year()