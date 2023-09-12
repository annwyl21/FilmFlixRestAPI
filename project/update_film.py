from connect import *
import user_data_validation

#filmID(integer), title(text), yearReleased(integer),rating(text),duration(integer),genre(text)

def get_fieldvalue(user_choice):
	if user_choice == 't':
		fieldname = 'table'
		fieldvalue = user_data_validation.get_title()
	elif user_choice == 'y':
		fieldname = 'yearReleased'
		fieldvalue = user_data_validation.get_release_year()
	elif user_choice == 'r':
		fieldname = 'rating'
		fieldvalue = user_data_validation.get_rating()
	elif user_choice == 'd':
		fieldname = 'duration'
		fieldvalue = user_data_validation.get_duration()
	elif user_choice == 'g':
		fieldname = 'genre'
		fieldvalue = user_data_validation.get_genre()
	else:
		fieldname = 'invalid'
		fieldvalue = 'exit'
	return fieldname, fieldvalue

def film_update():
	film_id_field = input('Enter Film Id\n')

	try:
		dbCursor.execute(f"SELECT * FROM tblfilms WHERE filmID = {film_id_field}")
		my_record = dbCursor.fetchone()
		print(my_record)

		if my_record == None:
			print(f"No record with film id {film_id_field}\n")
		
	except ValueError as e:
		print("Invalid film ID\n")
	
	user_choice = 'invalid'
	while user_choice not in ['t', 'y', 'r', 'd', 'g']:
		user_choice = input('Enter (t)itle, (y)ear Released, (r)ating, (d)uration, (g)enre or e(x)it\n').lower()
		fieldname, fieldvalue = get_fieldvalue(user_choice)
		if fieldvalue == 'exit':
			break

	# adding quotes earlier to prevent injection attack
	fieldvalue = "'" + str(fieldvalue) + "'"
	try:
		dbCursor.execute(f"UPDATE tblfilms SET {fieldname} = {fieldvalue} WHERE filmId = {film_id_field}")
		dbcon.commit()
	except sql.OperationalError as e:
		print("No database found")
		
	print(f"{film_id_field} updated")
