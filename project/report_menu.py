import show_all, select_by_genre, select_by_year, select_by_rating

def get_report_menu():
	with open("project/report_menu.txt", 'r') as reportMenu:
		readMenuContent = reportMenu.read()
	return readMenuContent

def report_menu():
	user_choice = 0
	
	while user_choice not in range(1,6):
		print(get_report_menu())
		user_choice = int(input("Enter selection:\n"))

		if user_choice not in range(1,6):
			print(f"{user_choice} not valid, please try again")
	
	return user_choice

def report_program():
	# flag_variable
	report_program = True

	while report_program:
		mainReportMenu = report_menu()

		if mainReportMenu == 1:
			show_all.get_films()
		elif mainReportMenu == 2:
			select_by_genre.select_genre()
		elif mainReportMenu == 3:
			select_by_year.select_year()
		elif mainReportMenu == 4:
			select_by_rating.select_rating()
		else:
			report_program = False

	print("Returning to Main Menu")
