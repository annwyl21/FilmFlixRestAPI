import crud_menu, report_menu, main_menu_queries

def get_menu():
	with open("project/main_menu.txt", 'r') as mainMenu:
		readMenuContent = mainMenu.read()

	return readMenuContent

def main_menu():

	#dynamic stats for main menu: count and sum of minutes
	film_count = main_menu_queries.get_database_length()
	print(f"\nFilm Flix Database holds {film_count} films")
	minutes = main_menu_queries.get_film_hours()
	print(f"That is {round(minutes/60)} hours of movies.\n") 

	user_choice = ''
	while user_choice.lower() not in ['o', 'r', 'x']:
		print(get_menu())
		user_choice = input("Enter selection:\n")

		if user_choice not in ['o', 'r', 'x']:
			print(f"{user_choice} not valid, please try again")
	
	return user_choice.lower()

# flag_variable
main_program = True

while main_program:
	mainMenu = main_menu()

	if mainMenu == 'o':
		crud_menu.crud_program()
	elif mainMenu == 'r':
	  	report_menu.report_program()
	else:
		main_program = False

print("Thank you for visiting Film Flix Database")