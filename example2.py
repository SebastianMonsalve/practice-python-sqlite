import sqlite3

con = sqlite3.connect("Movies.db")

cursor = con.cursor()

createTable = """
    CREATE TABLE Movies(
        Title VARCHAR,
        Year INT,
        Duration INT,
        Genre VARCHAR
    )
"""
cursor.execute("DROP TABLE IF EXISTS Movies")

cursor.execute(createTable)