import pytest
from user_data_check import UserDataCheck

# test SQL injections and code injections into all user entry fields
@pytest.mark.parametrize("SQLinjection, answer", [
	("; DROP DATABASE; --", "error"), #SQL injection
	(" OR 1=1 --", "error"), # SQL injection
	("<h1>hello</h1>", "error") # markup insertion
])
def test_check_SQLinjection(SQLinjection, answer):
	results = UserDataCheck.check_rating(SQLinjection, ['G', 'PG', '12A', '15', 'R'])
	assert results == answer, f"rating check failed SQLinjection"
	results = UserDataCheck.check_duration(SQLinjection)
	assert results == answer, f"duration check failed SQLinjection"
	results = UserDataCheck.check_year(SQLinjection)
	assert results == answer, f"year check failed SQLinjection"
	results = UserDataCheck.check_title(SQLinjection)
	assert results == answer, f"title check failed SQLinjection"
	results = UserDataCheck.check_film_id(SQLinjection)
	assert results == answer, f"film_id check failed SQLinjection"
	results = UserDataCheck.check_word(SQLinjection)
	assert results == answer, f"word check failed SQLinjection"


# FILM_ID field tests
def test_film_id_acceptable():
	film_id = "42"
	results = UserDataCheck.check_film_id(film_id)
	assert results == "42", f"film_id check not working {film_id}"

@pytest.mark.parametrize("film_id, answer", [
	("400", "error"), # too big
	("4d", "error"), # not a valid number
	("-4", "error"), # not a valid number
	("4.5", "error"), # not a valid number
])
def test_film_id_unacceptable(film_id, answer):
	results = UserDataCheck.check_film_id(film_id)
	assert results == answer, f"film_id check not working {film_id}"


# WORD field tests
@pytest.mark.parametrize("word, answer", [
	("pet", "pet"),
])
def test_word_check_acceptable(word, answer):
	results = UserDataCheck.check_word(word)
	assert results == answer, f"word check failed {word}"


# TITLE field tests
@pytest.mark.parametrize("title, answer", [
	("The Lost City", "The Lost City"), #String acceptable and can be used in database
	# The following all contain punctuation
	("Independence Day: Resurgence", "Independence Day: Resurgence"), # accept colon as part of title - edge case
])
def test_check_title_acceptable(title, answer):
	results = UserDataCheck.check_title(title)
	assert results == answer, f"title check failed {title}"


# YEAR field tests
@pytest.mark.parametrize("year, answer", [
	("2023", "2023"),
	("1888", "1888"),
])
def test_check_year_acceptable(year, answer):
	results = UserDataCheck.check_year(year)
	assert results == answer, f"year check failed {year}, {results}"

@pytest.mark.parametrize("year, answer", [
	("1850", "error"), # date too old
	#("25", 'error') # user must enter century
])
def test_check_year_unacceptable(year, answer):
	results = UserDataCheck.check_year(year)
	assert results == answer, f"year check failed {year}, {results}"


# DURATION field tests
@pytest.mark.parametrize("duration, answer", [
	("120", "120"),
	("873", "873"), # edge case, longest movie
	("1", "1"), # shortest possible length 1-min
])
def test_check_duration_acceptable(duration, answer):
	results = UserDataCheck.check_duration(duration)
	assert results == answer, f"duration check failed {duration}, {results}"

@pytest.mark.parametrize("duration, answer", [
	("0", "error"),
	#("1.20")
	#("1h20m")
])
def test_check_duration_unacceptable(duration, answer):
	results = UserDataCheck.check_duration(duration)
	assert results == answer, f"duration check failed {duration}, {results}"


# RATING field tests
@pytest.mark.parametrize("rating, answer", [
	("12a", "12A"), #String acceptable
])
def test_check_rating_acceptable(rating, answer):
	results = UserDataCheck.check_rating(rating, ['G', 'PG', '12A', '15', 'R'])
	assert results == answer, f"rating check failed {rating}, {results}"

@pytest.mark.parametrize("rating, answer", [
	("18", "error"), # 18 is not an accepted rating
])
def test_check_rating_unacceptable(rating, answer):
	results = UserDataCheck.check_rating(rating, ['G', 'PG', '12A', '15', 'R'])
	assert results == answer, f"rating check failed {rating}, {results}"


