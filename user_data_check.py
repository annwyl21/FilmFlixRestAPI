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
			if not word.isalnum():# allow colon as punctuation only
				for letter in word:
					if letter not in range(48, 58) or letter not in range(65, 90):
						return 'error'	
			else:
				return title


	# check year released
	# check rating
	# check duration
	# check genre
		
	@staticmethod
	def check_data_to_add(data):
		title = UserDataCheck.check_word(data.get('title'))
		year_released = data.get('year_released')
		rating = data.get('rating')
		duration = data.get('duration')
		genre = data.get('genre')
		return {'title': title, 'year_released': year_released, 'rating': rating, 'duration': duration, 'genre': genre}
		