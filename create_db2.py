import sqlite3

connection = sqlite3.connect('database2.db')

with open('schema2.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Insérer dans la table livres
cur.execute("INSERT INTO livres (id, created, titre, auteur, pret,stock) VALUES (?, ?, ?, ?, ?,?)",
            (1, 190325, 'A la recherche du temps perdu', 'Marcel Proust', 'disponible',3))
cur.execute("INSERT INTO livres (id, created, titre, auteur, pret,stock) VALUES (?, ?, ?, ?, ?,?)",
            (2, 190325, 'Notre dame de Paris', 'Victor Hugo', 'disponible',3))

# Insérer dans la table stock

# Insérer dans la table pret avec la date correctement formatée
cur.execute("INSERT INTO pret (id, created, titre, auteur, date_pret, utilisateur_pret) VALUES (?, ?, ?, ?, ?, ?)",
            (1, 190325, 'A la recherche du temps perdu', 'Marcel Proust', '2025-02-12', 'Dupond'))
cur.execute("INSERT INTO pret (id, created, titre, auteur, date_pret, utilisateur_pret) VALUES (?, ?, ?, ?, ?, ?)",
            (2, 190325, 'Notre dame de Paris', 'Victor Hugo', '2025-02-12', 'Martin'))

cur.execute ("INSERT INTO utilisateur (id,nom, email, mot_de_passe, role) VALUES (?,?, ?, ?, ?)", 
                       (1,'DUPONT', 'dupont@at.fr', 'password', 'utilisateur'))
cur.execute ("INSERT INTO utilisateur (id,nom, email, mot_de_passe, role) VALUES (?,?, ?, ?, ?)", 
                       (2,'DUPO', 'dupo@at.fr', 'passwords', 'utilisateur'))

connection.commit()
connection.close()
