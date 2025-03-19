
import sqlite3

connection = sqlite3.connect('database2.db')

with open('schema2.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO livres (id, created, titre, auteur, date_pret,utilisateur_pret) VALUES (?,?,?, ?, ?,?)",(1,190325,'A la recherche du temps perdu', 'Marcel Proust',' ',''))
cur.execute("INSERT INTO livres (id, created,titre, auteur, date_pret,utilisateur_pret) VALUES (?,?,?, ?, ?,?)",(2,190325,'Notre dame de Paris', 'Victor Hugo',' ',''))

connection.commit()
connection.close()
