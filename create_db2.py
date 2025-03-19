
import sqlite3

connection = sqlite3.connect('database2.db')

with open('schema2.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO livres (id, created, titre, auteur,pret) VALUES (?,?,?, ?)",(1,190325,'A la recherche du temps perdu', 'Marcel Proust','disponible'))
cur.execute("INSERT INTO livres (id, created,titre, auteur, date_pret,utilisateur_pret) VALUES (?,?,?, ?)",(2,190325,'Notre dame de Paris', 'Victor Hugo','oui'))
cur.execute("INSERT INTO stock (id, created, titre, auteur,quantite_en_stock) VALUES (?,?,?, ?, ?)",(1,190325,'A la recherche du temps perdu', 'Marcel Proust',2))
cur.execute("INSERT INTO stock (id, created, titre, auteur,quantite_en_stock) VALUES (?,?,?, ?, ?)",(2,190325,'Notre dame de Paris', 'Victor Hugo',3))
cur.execute("INSERT INTO pret (id, created, titre, auteur,date_pret,utilisateur_pret) VALUES (?,?,?, ?, ?,?)",(1,190325,'A la recherche du temps perdu','Marcel Proust',12/2/2025,'Dupond'))
cur.execute("INSERT INTO pret (id, created, titre, auteur,date_pret,utilisateur_pret) VALUES (?,?,?, ?, ?,?)",(2,190325,'Notre dame de Paris', 'Victor Hugo',12/2/2025,'Martin'))
connection.commit()
connection.close()
