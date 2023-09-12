import show_all, add_film, update_film, delete_film

menu_choices = ['p', 'a', 'u', 'd', 'r']

def get_menu():
	with open("project/crud_menu.txt", 'r') as crudMenu:
		readMenuContent = crudMenu.read()
	return readMenuContent

def crud_menu():
	user_choice = ''
	
	while user_choice.lower() not in menu_choices:
		print(get_menu())
		user_choice = input("Enter selection:\n")

		if user_choice not in menu_choices:
			print(f"{user_choice} not valid, please try again")
	
	return user_choice.lower()

def crud_program():
	# flag_variable
	crud_program = True

	while crud_program:
		mainFilmMenu = crud_menu()

		if mainFilmMenu == 'p':
			show_all.get_films()
		elif mainFilmMenu == 'a':
			add_film.insert_film()
		elif mainFilmMenu == 'u':
			update_film.film_update()
		elif mainFilmMenu == 'd':
			delete_film.delete_film()
		else:
			crud_program = False

	print("Returning to Main Menu")