import datetime

today = datetime.date.today()

class UserDataCheck:

	@staticmethod # self is not needed with a static method, no instantiation is required to use a static method
	def check_film_id(film_id):
		# check film id is a number
		if film_id.isnumeric() and (int(film_id) in range(0, 100)):
			return film_id
		else:
			return 'error'
	
	@staticmethod
	def check_word(word):
		#check word only contains letters or numbers and no punctuation
		if word.isalnum():
			return word
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
		return title
	
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
			if int(duration) > 1 and int(duration) < 874:
				return duration
			else:
				return 'error'
		except ValueError as e:
			return 'error'

	# check rating
	# check genre
		
	@staticmethod
	def check_data_to_add(data):
		title = UserDataCheck.check_word(data.get('title'))
		year_released = UserDataCheck.check_year(data.get('year_released'))
		rating = data.get('rating')
		duration = UserDataCheck.check_duration(data.get('duration'))
		genre = data.get('genre')
		return {'title': title, 'year_released': year_released, 'rating': rating, 'duration': duration, 'genre': genre}
	
