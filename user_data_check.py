class UserDataCheck:

	@staticmethod # self is not needed with a static method, no instantiation is required to use a static method
	def check_film_id(film_id):
		# check film id is a number
		if film_id.isnumeric() and (int(film_id) in range(0, 100)):
			return film_id
		else:
			return 'error'
		