import pytest
from user_data_check import UserDataCheck

def test_id():
	film_id = "42"
	results = UserDataCheck.check_film_id(film_id)
	assert results == "42", f"film_id check not working {film_id}"

@pytest.mark.parametrize("film_id, answer", [
	("42", "42"), # String acceptable and so should pass the check and be returned to use in the database
	("400", "error"), # too big
	("4d", "error"), # not a valid number
	("-4", "error"), # not a valid number
	("4.5", "error"), # not a valid number
])
def test_film_id(film_id, answer):
	results = UserDataCheck.check_film_id(film_id)
	assert results == answer, f"film_id check not working {film_id}"

@pytest.mark.parametrize("word, answer", [
	("pet", "pet"), #String acceptable and can be used in database
	# The following all contain punctuation
	("break;", "error"), # code injection
	("; DROP DATABASE; --", "error"), #SQL injection
	(" OR 1=1 --", "error"), # SQL injection
	("<h1>hello</h1>", "error") # markup insertion
])
def test_word_check(word, answer):
	results = UserDataCheck.check_word(word)
	assert results == answer, f"word check failed {word}"

@pytest.mark.parametrize("title, answer", [
	("The Lost City", "The Lost City"), #String acceptable and can be used in database
	# The following all contain punctuation
	("Independence Day: Resurgence", "Independence Day: Resurgence"), # accept colon as part of title - edge case
	("; DROP DATABASE; --", "error"), #SQL injection
	(" OR 1=1 --", "error"), # SQL injection
	("<h1>hello</h1>", "error") # markup insertion
])
def test_check_title(title, answer):
	results = UserDataCheck.check_title(title)
	assert results == answer, f"title check failed {title}"
	