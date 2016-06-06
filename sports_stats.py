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

def stat_output(data, query, key):
    for row in data:
        if query in str(row[key]):
            print("Name:", row["Full Name"])
            print("Position:", row["Position"])
            print("Age:", row["Age"])
            print("Number:", row["Number"])
            print("Games started:", row["Games Started"])
            print("Goals scored:", row["Goals Scored"])
            print("Assists:", row["Assists"])
            print("Yellow cards:", row["Yellow Cards"])
            print("Red cards:", row["Red Cards"], "\n")


#def wild_card_output(data, user_input, key):
    #for row in data:
        #if user_input in row[key]:
            #print(row)


def nice_display(data, user_input):
    for row in data:
        if user_input in row:
            print("Name:", row[0])
            print("Position:", row[1])
            print("Age:", row[2])
            print("Number:", row[3])
            print("Games started:", row[4])
            print("Goals scored:", row[5])
            print("Assists:", row[6])
            print("Yellow cards:", row[7])
            print("Red cards:", row[8], "\n")


def search_player_name():
    player_name = input("Please search by player name: ")
    cursor.execute("SELECT * FROM arsenal_2016_17_stats WHERE full_name = %s;",(player_name,))
    results = cursor.fetchall()
    nice_display(results, player_name)
    search = input("Would you like to search again? y/n: ")
    if search == "y":
        stat_search()
    else:
        control()


def add_player():
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
    nice_display(results, full_name)
    search = input("Would you like to add another player? y/n: ")
    if search == "y":
        wild_card_search()
    else:
        control()


def stat_search():
    keys = ["Full Name", "Position", "Age", "Number", "Games Started", "Goals Scored", "Assists", "Yellow Cards",
            "Red Cards"]
    cursor.execute("SELECT * FROM arsenal_2016_17_stats;")
    results = cursor.fetchall()
    player_stats_dicts = [dict(zip(keys, row)) for row in results]
    print("Which stat/attribute would you like to search for? 1. Number, 2. Position, 3. Age, 4. Goals Scored 5. Assists")
    stat_lookup = input(">> ")
    if stat_lookup == "1":
        name_lookup = input("Number: ")
        stat_output(player_stats_dicts, name_lookup, "Number")
    if stat_lookup == "2":
        position_lookup = input("Position: ")
        stat_output(player_stats_dicts, position_lookup, "Position")
    if stat_lookup == "3":
        age_lookup = input("Age: ")
        stat_output(player_stats_dicts, age_lookup, "Age")
    if stat_lookup == "4":
        number_lookup = input("Goals Scored: ")
        stat_output(player_stats_dicts, number_lookup, "Goals Scored")
    if stat_lookup == "5":
        number_lookup = input("Assists: ")
        stat_output(player_stats_dicts, number_lookup, "Goals Scored")
    search = input("Would you like to search again? y/n: ")
    if search == "y":
        stat_search()
    else:
        control()


def wild_card_search():
    search_wild_card = input("Please enter keyword: ")
    keys = ["Full Name", "Position", "Age", "Number", "Games Started", "Goals Scored", "Assists", "Yellow Cards",
            "Red Cards"]
    cursor.execute("SELECT * FROM arsenal_2016_17_stats;")
    results = cursor.fetchall()
    player_stats_dicts = [dict(zip(keys, row)) for row in results]
    stat_output(player_stats_dicts, search_wild_card, "Full Name")
    stat_output(player_stats_dicts, search_wild_card, "Position")
    stat_output(player_stats_dicts, search_wild_card, "Age")
    stat_output(player_stats_dicts, search_wild_card, "Number")
    stat_output(player_stats_dicts, search_wild_card, "Games Started")
    stat_output(player_stats_dicts, search_wild_card, "Goals Scored")
    stat_output(player_stats_dicts, search_wild_card, "Assists")
    stat_output(player_stats_dicts, search_wild_card, "Yellow Cards")
    stat_output(player_stats_dicts, search_wild_card, "Red Cards")
    search = input("Would you like to search again? y/n: ")
    if search == "y":
        wild_card_search()
    else:
        control()


def top_players():
    print("Find top players in... 1. goals scored, 2. assists: ")
    user_input = input(">> ")
    if user_input == "1":
        cursor.execute("SELECT * FROM arsenal_2016_17_stats ORDER BY goals_scored DESC;")
        results = cursor.fetchall()
        for row in results:
            print(row[0],":", row[5])
    if user_input == "2":
        cursor.execute("SELECT * FROM arsenal_2016_17_stats ORDER BY assists DESC;")
        results = cursor.fetchall()
        for row in results:
            print(row[0],":", row[6])


def control():
    print("Would you like to... 1. search player name, 2. search stat, 3. search wild card, 4. add new player, 5. search top performers")
    user_input = input(">> ")
    if user_input == "1":
        search_player_name()
    if user_input == "2":
        stat_search()
    if user_input == "3":
        wild_card_search()
    if user_input == "4":
        add_player()
    if user_input == "5":
        top_players()

control()
#stat_search()
#search_player_name()
#add_player()
#wild_card_search("CM")
#top_players()


cursor.close()
connection.close()


