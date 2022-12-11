import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

current = connection.cursor()

current.execute("INSERT INTO teams (name) VALUES ('Team1')")
current.execute("INSERT INTO teams (name) VALUES ('Team2')")

current.execute("INSERT INTO players (name, team) VALUES (?,?)", ('Gigi', 'Team1'))
current.execute("INSERT INTO players (name, team) VALUES (?,?)", ('Ion', 'Team1'))
current.execute("INSERT INTO players (name, team) VALUES (?,?)", ('Zahar', 'Team1'))
current.execute("INSERT INTO players (name, team) VALUES (?,?)", ('Lalea', 'Team2'))
current.execute("INSERT INTO players (name, team) VALUES (?,?)", ('Mia', 'Team2'))
current.execute("INSERT INTO players (name, team) VALUES (?,?)", ('Sesea', 'Team2'))

connection.commit()
connection.close()