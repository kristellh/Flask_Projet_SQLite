from flask import Flask, render_template_string, render_template, jsonify, request, redirect, url_for, session
from flask import render_template
from flask import json
from urllib.request import urlopen
from werkzeug.utils import secure_filename
import sqlite3

app = Flask(__name__)                                                                                                                  
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Clé secrète pour les sessions

# Fonction pour créer une clé "authentifie" dans la session utilisateur
def est_authentifie():
    return session.get('authentifie')

@app.route('/accueil')
def accueil():
    return render_template('accueil.html')

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/lecture')
def lecture():
    if not est_authentifie():
        # Rediriger vers la page d'authentification si l'utilisateur n'est pas authentifié
        return redirect(url_for('authentification'))

  # Si l'utilisateur est authentifié
    return "<h2>Bravo, vous êtes authentifié</h2>"

@app.route('/authentification', methods=['GET', 'POST'])
def authentification():
    if request.method == 'POST':
        # Vérifier les identifiants
        if request.form['username'] == 'admin' and request.form['password'] == 'password': # password à cacher par la suite
            session['authentifie'] = True
            # Rediriger vers la route lecture après une authentification réussie
            return redirect(url_for('lecture'))
        else:
            # Afficher un message d'erreur si les identifiants sont incorrects
            return render_template('formulaire_authentification.html', error=True)

    return render_template('formulaire_authentification.html', error=False)

@app.route('/fiche_client/<int:post_id>')
def Readfiche(post_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients WHERE id = ?', (post_id,))
    data = cursor.fetchall()
    conn.close()
    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', data=data)

@app.route('/fiche_livre/<int:post_id>')
def Readfiche2(post_id):
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livres WHERE id = ?', (post_id,))
    data = cursor.fetchall()
    conn.close()
    # Rendre le template HTML et transmettre les données
    return render_template('read_data2.html', data=data)
    
@app.route('/consultation/')
def ReadBDD():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients;')
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data.html', data=data)

@app.route('/consultation_livre/')
def ReadBDD2():
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livres;')
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data2.html', data=data)

@app.route('/enregistrer_client', methods=['GET'])
def formulaire_client():
    return render_template('formulaire.html') 
    
    
@app.route('/enregistrer_livre', methods=['GET'])
def formulaire_livre():
    return render_template('formulaire_livre.html') # afficher le formulaire

@app.route('/supprimer_livre', methods=['GET'])
def supprimer_livre():
    return render_template('supprimer_livre.html')  # afficher le formulaire
# afficher le formulaire

@app.route('/recherche_livre', methods=['GET'])
def rechercher_livre():
    return render_template('recherche_livre.html')

@app.route('/enregistrer_client', methods=['POST'])
def enregistrer_client():
    nom = request.form['nom']
    prenom = request.form['prenom']

    # Connexion à la base de données
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Exécution de la requête SQL pour insérer un nouveau client
    cursor.execute('INSERT INTO clients (created, nom, prenom, adresse) VALUES (?, ?, ?, ?)', (1002938, nom, prenom, "ICI"))
    conn.commit()
    conn.close()
    return redirect('/consultation/')  # Rediriger vers la page d'accueil après l'enregistrement


@app.route('/enregistrer_livre', methods=['POST'])
def enregistrer_livre():
    titre = request.form['titre']
    auteur = request.form['auteur']

    # Connexion à la base de données
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()

    # Exécution de la requête SQL pour insérer un nouveau client
    cursor.execute('INSERT INTO livres (created,titre, auteur,pret) VALUES (?,?,?, ?)', (190325,titre, auteur,"disponible"))
    conn.commit()
    conn.close()
    return redirect('/consultation_livre/')  # Rediriger vers la page d'accueil



@app.route('/supprimer_livre', methods=['POST'])
def supprimer_livre_post():
    titre = request.form['titre']
    auteur = request.form['auteur']
    id = request.form['id']

    # Connexion à la base de données
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()

    # Suppression en fonction du titre, auteur ou id
    if id:  # Si un id est fourni, supprimer par id
        cursor.execute('DELETE FROM livres WHERE id = ?', (id,))
    else:  # Sinon, supprimer par titre et auteur
        cursor.execute('DELETE FROM livres WHERE titre = ? AND auteur = ?', (titre, auteur))

    conn.commit()
    conn.close()

    # Rediriger vers la page de consultation après la suppression
    return redirect('/consultation_livre/')


@app.route('/recherche_livre', methods=['POST'])
def rechercher_livre_post():
    titre = request.form['titre']
    auteur = request.form['auteur']
    id = request.form['id']

    # Connexion à la base de données
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()

    # Recherche en fonction de l'id
    if id:  
        cursor.execute('SELECT * FROM livres WHERE id = ?', (id,))
        livre = cursor.fetchone()  
        if livre:
           
            return redirect(f'/fiche_livre/{livre[0]}') 
        else:
          
            return redirect('/consultation_livre/')

    elif titre and auteur:  
        cursor.execute('SELECT * FROM livres WHERE titre = ? AND auteur = ?', (titre, auteur))
        livre = cursor.fetchone() 
        if livre:
         
            return redirect(f'/fiche_livre/{livre[0]}')  
        else:
       
            return redirect('/consultation_livre/')
    else:
        return redirect('/consultation_livre/')
 
    conn.close()  

@app.route('/fiche_utilisateur/<int:post_id>')
def Readfiche3(post_id):
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM utilisateur WHERE id = ?', (post_id,))
    data = cursor.fetchall()
    conn.close()
    # Rendre le template HTML et transmettre les données
    return render_template('read_data3.html', data=data)
    


@app.route('/consultation_utilisateur/')
def ReadBDD3():
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM utilisateur;')
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data3.html', data=data)

@app.route('/enregistrer_utilisateur', methods=['GET'])
def formulaire_utilisateur():
    return render_template('enregistrer_utilisateur.html') 
    
@app.route('/enregistrer_utilisateur', methods=['POST'])
def formulaire_utilisateur_post():
    nom = request.form['nom']
    email = request.form['email']
    mot_de_passe = request.form['mot_de_passe']

    # Connexion à la base de données
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()

    # Exécution de la requête SQL pour insérer un nouveau utilisateur
    cursor.execute('INSERT INTO utilisateur (nom,email,mot_de_passe,role) VALUES (?,?,?,?)', 
                   (nom, email,mot_de_passe,'utilisateur'))
    conn.commit()
    conn.close()
    return redirect('/consultation_utilisateur/')


@app.route('/supprimer_utilisateur', methods=['GET'])
def supprimer_utilisateur():
    return render_template('supprimer_utilisateur.html')  # afficher le formulaire
# afficher le formulaire
@app.route('/supprimer_utilisateur', methods=['POST'])
def supprimer_utilisateur_post():
    nom = request.form['nom']
    email= request.form['email']
    id = request.form['id']

    # Connexion à la base de données
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()

    # Suppression en fonction du titre, auteur ou id
    if id:  # Si un id est fourni, supprimer par id
        cursor.execute('DELETE FROM utilisateur WHERE id = ?', (id,))
    else:  # Sinon, supprimer par titre et auteur
        cursor.execute('DELETE FROM utilisateur WHERE nom = ? AND email = ?', (nom, email))

    conn.commit()
    conn.close()

    # Rediriger vers la page de consultation après la suppression
    return redirect('/consultation_utilisateur/')

@app.route('/recherche_utilisateur', methods=['GET'])
def rechercher_utilisateur():
    return render_template('recherche_utilisateur.html')
@app.route('/recherche_utilisateur', methods=['POST'])
def rechercher_utilisateur_post():
    nom = request.form['nom']
    email= request.form['email']
    id = request.form['id']

    # Connexion à la base de données
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()

    # Recherche en fonction de l'id
    if id:  
        cursor.execute('SELECT * FROM utilisateur WHERE id = ?', (id,))
        livre = cursor.fetchone()  
        if livre:
           
            return redirect(f'/fiche_utilisateur/{utilisateur[0]}') 
        else:
          
            return redirect('/consultation_utilisateur/')

    elif titre and auteur:  
        cursor.execute('SELECT * FROM utilisateur WHERE nom = ? AND email = ?', (nom, email))
        livre = cursor.fetchone() 
        if livre:
         
            return redirect(f'/fiche_utilisateur/{utilisateur[0]}')  
        else:
       
            return redirect('/consultation_utilisateur/')
    else:
        return redirect('/consultation_utilisateur/')
 
    conn.close() 
@app.route('/liste_livre', methods=['GET'])
def liste_livre():
    return render_template('liste_livre.html') 

@app.route('/liste_livres', methods=['GET'])
def liste_livres():
    # Connexion à la base de données
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()

    # Récupérer la liste des livres avec leur stock
    cursor.execute("""
        SELECT livre.id, livre.titre, livre.auteur, stock.quantite_en_stock
        FROM livre
        JOIN stock ON livre.id = stock.id
    """)
    livre = cursor.fetchall()

    # Fermer la connexion
    conn.close()

    # Si aucun livre n'est trouvé, renvoyer un message
    if not livre:
        return "Aucun livre trouvé dans le stock.", 404

    # Retourner la page HTML avec la liste des livres
    return render_template('liste_livres.html', livres=livres)


@app.route('/mettre_a_jour_stock', methods=['POST'])
def mettre_a_jour_stock():
    livre_id = request.form['livre_id']
    quantite = int(request.form['quantite'])

    # Connexion à la base de données
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()

    # Vérifier si le livre existe dans la table stock
    cursor.execute("SELECT quantite_en_stock FROM stock WHERE livre_id = ?", (livre_id,))
    stock = cursor.fetchone()

    if stock is None:
        # Si le livre n'est pas encore dans le stock, ajouter une nouvelle entrée
        cursor.execute("INSERT INTO stock (livre_id, quantite_en_stock) VALUES (?, ?)", (livre_id, quantite))
    else:
        # Si le livre est déjà dans le stock, mettre à jour la quantité
        new_quantite = stock[0] + quantite  # Ajoute la quantité spécifiée
        cursor.execute("UPDATE stock SET quantite_en_stock = ? WHERE livre_id = ?", (new_quantite, livre_id))

    # Commit et fermeture de la connexion
    conn.commit()
    conn.close()

    # Rediriger vers la page des livres après la mise à jour
    return redirect('/liste_livre')


if __name__ == "__main__":
  app.run(debug=True)
