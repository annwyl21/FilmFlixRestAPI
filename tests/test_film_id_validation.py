import pytest
from user_data_check import UserDataCheck

@pytest.mark.parametrize("film_id, answer", [
	("42", "42"), # The string '42' is acceptable and so should pass the check and be returned to use in the database
	("400", "error"), # too big
	("4d", "error"), # not a valid number
	#("-4", "error"), # not a valid number
	#("4.5", "error"), # not a valid number
])
def test_film_id(film_id, answer):
	results = UserDataCheck.check_film_id(film_id)
	assert results == answer, f"film_id check not working {answer}"

def test_id():
	film_id = "42"
	results = UserDataCheck.check_film_id(film_id)
	assert results == "42", f"film_id check not working {film_id}"