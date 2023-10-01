import datetime

today = datetime.date.today()

class UserDataCheck:

	@staticmethod # self is not needed with a static method, no instantiation is required to use a static method
	def check_film_id(film_id):
		# check film id is a number
		if film_id.isnumeric():
			return film_id
		else:
			return 'error'
	
	@staticmethod
	def check_word(word):
		word = word.lower()
		#check word/ genre single word only contains letters or numbers and no punctuation or spaces
		if word.isalnum():
			return word.title()
		else:
			return 'error'
		
	@staticmethod
	def check_title(title):
		words_in_title = title.split()
		for word in words_in_title:
			word = word.lower()
			# allow colon as punctuation only
			for letter in word:
				if not (letter.islower() or letter.isdigit() or letter == ':'):
					return 'error'
		return title.title()
	
	@staticmethod
	def check_year(year):
		try:
			if int(year) >= 1888 and int(year) <= today.year:
				return year
			else:
				return 'error'
		except ValueError as e:
			return 'error'
	
	@staticmethod
	def check_duration(duration):
		try:
			if int(duration) >= 1 and int(duration) < 874:
				print(duration, type(duration))
				return duration
			else:
				return 'error'
		except ValueError as e:
			return 'error'
		
	@staticmethod
	def check_rating(rating, available_ratings):
		rating = rating.upper()
		# list contains standardised ratings used in the database
		if rating in available_ratings:
			return rating
		else:
			return 'error'

		
	@staticmethod
	def check_data_to_add(data, available_ratings):
		title = UserDataCheck.check_title(data['title'])
		year_released = UserDataCheck.check_year(data['year_released'])
		rating = UserDataCheck.check_rating(data['rating'], available_ratings)
		duration = UserDataCheck.check_duration(data['duration'])
		genre = UserDataCheck.check_word(data['genre'])
		return {'title': title, 'year_released': year_released, 'rating': rating, 'duration': duration, 'genre': genre}
	
