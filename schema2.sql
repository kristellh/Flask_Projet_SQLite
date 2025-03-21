DROP TABLE IF EXISTS livres;
CREATE TABLE livres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    titre TEXT NOT NULL,
    auteur TEXT NOT NULL,
    pret TEXT NOT NULL,
    stock INTEGER
);
DROP TABLE IF EXISTS stock;
CREATE TABLE stock (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    livre_id INTEGER,
    quantite_en_stock INTEGER,
    FOREIGN KEY(livre_id) REFERENCES livres(id)
);

DROP TABLE IF EXISTS pret;
CREATE TABLE pret (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    titre TEXT NOT NULL,
    auteur TEXT NOT NULL,
    date_pret DATE NOT NULL,  -- Change ici pour le type DATE
    utilisateur_pret TEXT NOT NULL
);
DROP TABLE IF EXISTS utilisateur;
CREATE TABLE utilisateur (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    mot_de_passe TEXT NOT NULL,
    role TEXT DEFAULT 'utilisateur'
);
