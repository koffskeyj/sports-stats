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

#cursor.execute("INSERT INTO arsenal_2016_17_stats VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"(full_name, position, age, number, games_started, goals_scored, assists, yellow_cards, red_cards))


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


#cursor.execute("SELECT * FROM arsenal_2016_17_stats));"

def search_player_name():
    player_name = input("Please search by player name: ")
    cursor.execute("SELECT * FROM arsenal_2016_17_stats WHERE full_name = %s;",(player_name,))
    results = cursor.fetchall()
    print(results)
    for row in results:
        if player_name in row:
            print("Name:", row[0])
            print("Position:", row[1])
            print("Age:", row[2])
            print("Number:", row[3])
            print("Games started:", row[4])
            print("Goals scored:", row[5])
            print("Assists:", row[6])
            print("Yellow cards:", row[7])
            print("Red cards:", row[8])


def add_player():
    new_player = input("Would you like to add a new player? y/n: ")
    if new_player == "y":
        full_name = input("Please input player name: ")
        position = input("Please input player position: ")
        age = int(input("Please input player age: "))
        number = int(input("Please input player number: "))
        games_started = int(input("Please input games started: "))
        goals_scored = int(input("Please input goals scored: "))
        assists = int(input("Please input assists made: "))
        yellow_cards = int(input("Please input amount of yellow cards: "))
        red_cards = int(input("Please input amount of red cards: "))

        cursor.execute("INSERT INTO arsenal_2016_17_stats VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);",(full_name, position, age, number, games_started, goals_scored,assists, yellow_cards, red_cards))
        connection.commit()
        cursor.execute("SELECT * FROM arsenal_2016_17_stats;")
        results = cursor.fetchall()
        for row in results:
            print([row])
    if new_player == "n":
        search_player_name()


def wild_card_search():
    search_wild_card = input("Please enter search keyword: ")
    keys = ["Full Name", "Position", "Age", "Number", "Games Started", "Goals Scored", "Assists", "Yellow Cards",
            "Red Cards"]
    cursor.execute("SELECT * FROM arsenal_2016_17_stats;")
    results = cursor.fetchall()
    player_stats_dicts = [dict(zip(keys, row)) for row in results]
    for i in player_stats_dicts:
        if search_wild_card in i["Full Name"]:
            print(i)
        if search_wild_card in i["Position"]:
            print(i)
        if search_wild_card in str(i["Age"]):
            print(i)
        if search_wild_card in str(i["Number"]):
            print(i)
        if search_wild_card in str(i["Games Started"]):
            print(i)
        if search_wild_card in str(i["Goals Scored"]):
            print(i)
        if search_wild_card in str(i["Assists"]):
            print(i)
        if search_wild_card in str(i["Yellow Cards"]):
            print(i)
        if search_wild_card in str(i["Red Cards"]):
            print(i)

    #any(i['Full Name'] == search_wild_card for i in player_stats_dicts)







#add_player()
wild_card_search()


cursor.close()
connection.close()


