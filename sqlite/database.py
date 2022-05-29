import sqlite3

# conn = sqlite3.connect(":memory") # to run in memory
# connect to db ## create database when python file is run
conn = sqlite3.connect("movie.db")

# create a cursor ## its a variable

c = conn.cursor()

# create a table
# use document string """  3 inverted commas for multiple lines
# if use " ## place everything in one line
# DATATYPE only 5
# NULL empty unknown
# INTEGER 0-9 numbers
## REAL - decimals
# TEXT - TEXT // string maybe
# BLOB image,mp3 files i guess

c.execute("""CREATE TABLE actor (
    act_id text,
    act_name text,
    act_gender text
    )""")

# insert for one is c.execute("INSERT INTO actor VALUES (301,'ANUSHKA','F')")

many_actors = [
(301,'ANUSHKA','F'),
(302,'PRABHAS','M'),
(303,'PUNITH','M'),
(304,'JERMY','M')
]
c.executemany("INSERT INTO actor VALUES (?,?,?)",many_actors)
print("inserted actor details successfully")
c.execute("SELECT * FROM actor")
item = c.fetchall() ## fetch all
for i in item : ## for one line at a time print statement
    print(i)

print("\n all actor name's displayed \n")
c.execute("""CREATE TABLE movies (
    movie_id text,
    movie_title text,
    movie_lang text,
    movie_year integer
    )""")

many_movies = [ ('1001','BAHUBALI-2', 2017, 'TELAGU'),
 ('1002','BAHUBALI-1', 2015, 'TELAGU'),
('1003','AKASH', 2008, 'KANNADA'),
 ('1004','WAR HORSE', 2011, 'ENGLISH')
]
#
print("insert movie successfully")
#
c.executemany("INSERT INTO movies VALUES (?,?,?,?)",many_movies)

#to select / display // include in print fucntion
c.execute("SELECT * FROM movies ")
# print(c.fetchone()[0]) ## fetch first item with 0th index
# print(c.fetchmany(3)) ## fetch index speicified
item = c.fetchall() ## fetch all
for i in item : ## for one line at a time print statement
    print(i)

print("\n all movie name's displayed \n")

# director details
c.execute("""CREATE TABLE director (
        director_id text,
        director_name text,
        director_number integer)
""")

many_directors = [
 ('60','RAJAMOULI', 8751611001),
('61','HITCHCOCK', 7766138911),
('62','FARAN', 9986776531),
 ('63','STEVEN SPIELBERG', 8989776530)
]
#
#insert into director
c.executemany("INSERT INTO director VALUES(?,?,?)",many_directors)
print("\n inserted director details successfully")

# directors details display
c.execute("SELECT * FROM director")
item = c.fetchall()
for i in item :
    print(i)

print("\n director details displayed successfully \n")

print("\n Only actor/actress name with gender \n")
c.execute("SELECT * FROM actor")
item = c.fetchall()
for i in item :
    print(i[1],i[2])

print("\n movie titles and their corressponding  release year,movie language\n")
c.execute("SELECT * FROM movies")
item = c.fetchall()
for i in item :
    print(i[1],i[2],i[3])

print("\n director names \n")
c.execute("SELECT * FROM director")
item = c.fetchall()
for i in item :
    print(i[1])


# Commmit our command
conn.commit()

# close our connection
conn.close()
