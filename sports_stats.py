import psycopg2

connection = psycopg2.connect("dbname=learning_sql user=dbperson")

cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS arsenal_2016_17_stats")

table_create_command = """CREATE TABLE arsenal_2016_17_stats(
  full_name varchar(30),
  position varchar(3),
  age numeric(3),
  number numeric(2),
  games_started numeric(2),
  goals_scored numeric(2),
  assists numeric(2),
  yellow_cards numeric(2),
  red_cards numeric(1)
);"""

cursor.execute(table_create_command)

#full_name = "Hector Bellerin"
#position = "RB"
#age = 21
#number = 24
#games_started = 36
#goals_scored = 1
#assists = 5
#yellow_cards = 3
#red_cards = 0

#cursor.execute("INSERT INTO arsenal_2016_17_stats VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);", \
               #(full_name, position, age, number, games_started, goals_scored, assists, yellow_cards, red_cards))


cursor.execute("INSERT INTO arsenal_2016_17_stats VALUES('Hector Bellerin', 'RB', 21, 24, 36, 1, 5, 3, 0),"
               "('Nacho Monreal', 'LB', 30, 18, 36, 0, 3, 1, 0),"
               "('Mesut Ozil', 'CAM', 27, 11, 35, 6, 19, 4, 0),"
               "('Laurent Koscielny', 'CB', 30, 6, 33, 4, 0, 3, 0),"
               "('Aaron Ramsey', 'CM', 25, 16, 29, 5, 4, 4, 0),"
               "('Alexis Sanchez', 'F', 27, 17, 28, 13, 4, 1, 0),"
               "('Olivier Giroud', 'ST', 29, 12, 26, 12, 6, 2, 0),"
               "('Per Mertesacker', 'CB', 31, 4, 24, 0, 0, 1, 1),"
               "('Francis Coquelin', 'CDM', 25, 34, 21, 0, 0, 5, 1),"
               "('Gabriel Paulista', 'CB', 25, 5, 18, 1, 0, 4, 1),"
               "('Theo Walcott', 'W', 27, 15, 14, 5, 2, 0, 0),"
               "('Santi Cazorla', 'CAM', 31, 19, 15, 0, 3, 2, 1),"
               "('Mathieu Flamini', 'CDM', 32, 20, 12, 0, 0, 3, 0),"
               "('Joel Campbell', 'W', 23, 28, 11, 3, 2, 0, 0),"
               "('Alex Oxlade-Chamberlain', 'W', 22, 15, 9, 1, 0, 0, 0);")

connection.commit()

cursor.execute("SELECT * FROM arsenal_2016_17_stats")
results = cursor.fetchall()
for row in results:
    print(row)

cursor.close()
connection.close()