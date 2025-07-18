import sqlite3

#create conection to the database
# if the database does not exist, it will be created
conexion = sqlite3.connect("mybasedata1")


# execute sql sentences
cursor = conexion.cursor()


# create table
# cursor.execute("""
#                CREATE TABLE students(
#                    Name TEXT,
#                    LastName TEXT,
#                    Age INT,
#                    Email TEXT,
#                    Id VARCHAR(20)
#                )
#                """)


# insert data into the table
# cursor.execute("INSERT INTO students(Name, LastName, Age, Email, Id) VALUES ('Sebastian', 'Monsalve', 22, 'jsmonsalvec16@gmail.com', 1)")

# commit the changes
# this is necessary to save the changes made to the database
# conexion.commit()


# query the table
# this will return all the rows in the table
datos = cursor.execute("SELECT * FROM students")
# fetch all rows from the query
for row in datos:
    print(row)


# close the connection
conexion.close()