# RestAPI connecting to a database of films in SQLite

Deployed to Render, my microservice can communicate with any client using **json** via its POST, PATCH, DELETE endpoints.
- 2 example clients that interact with the RestAPI
    - Web GUI Flask App to perform CRUD operations
    - Jupyter Notebook to display statistics about the database

# [Jupyter Notebook](https://github.com/annwyl21/FilmFlixRestAPI/blob/main/database_statistics.ipynb)

# [Web GUI Flask App](https://filmflixui.onrender.com/)
_Render does take a minute to spin up because I use the free service_

## RestAPI Features

- Logging of CRUD activities in .log file
- Testing
    - 23 parametrized unit tests in Pytest check multiple data entry possibilities including SQL injections
- CI/ CD 
    - A GitHub workflow runs tests in Pytest on every **pull request**

### Database Integrity
- Dynamically generated lists are used for data entry to help ensure data integrity
- Several Layers of data validation:
    - HTML validation of user entered data
    - Validation checks within the RestAPI that runs when data is received as json
    - The validation in the RestAPI is checked with tests that run automatically on pull request, to ensure there is always working code in the RestAPI
    - RestAPI uses parameterized queries to ensure user input is always treated as data and not as executable code
