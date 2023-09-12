from connect import *
import user_data_validation

def select_rating():
	rating = user_data_validation.get_rating()

	dbCursor.execute(f"SELECT * FROM tblfilms where rating = '{rating}'")

	all_records = dbCursor.fetchall()

	for each_record in all_records:
		print(each_record)

if __name__ == '__main__':
	select_rating()