from connect import *

def delete_film():

	film_ID_field = input("Select ID of Film to DELETE\n")

	try:
		dbCursor.execute(f"SELECT * FROM tblfilms WHERE filmID = {film_ID_field}")
		my_record = dbCursor.fetchone()

		if my_record == None:
			print(f"No record with film id {film_ID_field}\n")
		else:
			dbCursor.execute(f"DELETE FROM tblfilms where filmID = {film_ID_field}")
			dbcon.commit()
	
	except ValueError as e:
		print("Invalid film ID\n")

	# except sql.OperationalError as e:
	# 	print("No database found")
