import sqlite3

connection = sqlite3.connect('database2.db')

with open('schema2.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Insérer dans la table livres
cur.execute("INSERT INTO livres (id, created, titre, auteur, pret) VALUES (?, ?, ?, ?, ?)",
            (1, 190325, 'A la recherche du temps perdu', 'Marcel Proust', 'disponible'))
cur.execute("INSERT INTO livres (id, created, titre, auteur, pret) VALUES (?, ?, ?, ?, ?)",
            (2, 190325, 'Notre dame de Paris', 'Victor Hugo', 'disponible'))

# Insérer dans la table stock
cur.execute("INSERT INTO stock (id, created, titre, auteur, quantite_en_stock) VALUES (?, ?, ?, ?, ?)",
            (1, 190325, 'A la recherche du temps perdu', 'Marcel Proust', 2))
cur.execute("INSERT INTO stock (id, created, titre, auteur, quantite_en_stock) VALUES (?, ?, ?, ?, ?)",
            (2, 190325, 'Notre dame de Paris', 'Victor Hugo', 3))

# Insérer dans la table pret avec la date correctement formatée
cur.execute("INSERT INTO pret (id, created, titre, auteur, date_pret, utilisateur_pret) VALUES (?, ?, ?, ?, ?, ?)",
            (1, 190325, 'A la recherche du temps perdu', 'Marcel Proust', '2025-02-12', 'Dupond'))
cur.execute("INSERT INTO pret (id, created, titre, auteur, date_pret, utilisateur_pret) VALUES (?, ?, ?, ?, ?, ?)",
            (2, 190325, 'Notre dame de Paris', 'Victor Hugo', '2025-02-12', 'Martin'))

cur.execute ("INSERT INTO utilisateurs (nom, email, mot_de_passe, role) VALUES (?, ?, ?, ?)", 
                       ('DUPONT', 'dupont@at.fr', 'hashed_password', 'utilisateur'))
cur.execute ("INSERT INTO utilisateurs (nom, email, mot_de_passe, role) VALUES (?, ?, ?, ?)", 
                       ('DUPO', 'dupo@at.fr', 'hashed_password', 'utilisateur'))

connection.commit()
connection.close()
