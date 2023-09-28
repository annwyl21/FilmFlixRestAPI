# Extended Bootcamp Project - Film Flix Database

### PROJECT BRIEF: Build a python app to handle CRUD operations on a given database - Film Flix

I extended this project by building a python microservice that provides endpoints to an SQLite database of film data.
- My RestAPI is available on render 
	- [RestAPI on render](https://filmflixrestapi.onrender.com/api/films)
	- My microservice can communicate with any client using json via its POST, PATCH, DELETE endpoints.

I further extended this project by building 2 example clients; a jupyter notebook using Matplotlib to graph the database data and a flask app to provide a web GUI for the CRUD operations.

1. [Jupyter Notebook](https://github.com/annwyl21/FilmFlixRestAPI/blob/main/database_statistics.ipynb)

2. [Web GUI Flask App](https://github.com/annwyl21/FilmFlixUI)

3. Logging

4. Testing Pytest

5. CI/CD GitHub Actions
	
*I have better examples of Flask App UI's, this is purely to focus on demonstrating my knowledge of back-end operations.*

### Initial Bootcamp Project:

My more robust python command line app can be found on replit:

- [command line app on replit](https://replit.com/@EllenAsh1/ChocolateDigitalDecagons)
- manages basic CRUD operations
- can handle user-input mistakes
- has a logging output which logs when CRUD operations are performed
- string formatting for command line results

**Data Integrity Considerations for the Database:**

1. **Rating Field**:
    - The categorisation of the 'rating' field has been standardized based on a predefined list from the database: [G, PG, 12A, 15, R].
    - Measures have been implemented to ensure consistency by restricting user input to the aforementioned standardized list.

2. **Genre Field**:
    - The 'genre' field is designed with adaptability in mind. An initial list of genres is presented to users as a guideline.
    - Users have the liberty to introduce new genres. Any addition of new genres triggers a logging mechanism, serving as an added layer of data integrity verification.

I would engage in a collaborative discussion with the client to ascertain tailored needs, which would inform strategy for encoding these fields. This document showcases both a rigid and a malleable approach to data handling for these fields.