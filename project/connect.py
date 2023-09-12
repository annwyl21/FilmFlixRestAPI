import sqlite3 as sql # sql lite module

# db con is a variable that is initialised with everything on the right
dbcon = sql.connect("project/filmflix.db") # connect method create new or use an existing db

# assign cursor method to dbCursor to allow us to execute/ run sql queries and statements
dbCursor = dbcon.cursor()