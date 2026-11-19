import datetime

def date_future(nb_jours):
    """Renvoie la date située nb_jours après aujourd'hui"""
    return datetime.date.today() + datetime.timedelta(days=nb_jours)

# Constante contenant les délais en jours pour chaque niveau (index 0 à 4)
DELAIS = [1, 3, 7, 15, 30]

class Carte:

    def __init__(self, question, reponse):
        self.question = question
        self.reponse = reponse
        self.niveau = 0
        # À la création, la carte est à réviser le jour même
        self.date_prochaine = datetime.date.today()

    def __repr__(self):
        return f"<Carte: {self.question} (Niveau {self.niveau})>"

    # Question 1. Écrire ci-dessous la méthode traiter_reponse(self, succes)
    def traiter_reponse(self, succes):
        pass # à remplacer par votre code
  
###############################################################################
# Question 1. Tests pour la méthode traiter_reponse                           #
###############################################################################

def test_traiter_reponse():
    c1 = Carte("Capitale de l'Italie ?", "Rome")
    c1.niveau = 2
    c2 = Carte("7 x 8 ?", "56")
    c2.niveau = 4
    c1.traiter_reponse(True)
    assert c1.niveau == 3
    c1.traiter_reponse(False)
    assert c1.niveau == 0
    c2.traiter_reponse(True)
    assert c2.niveau == 4

###############################################################################
# Question 2. Écrire la fonction extraire_cartes_du_jour                      #
###############################################################################

def extraire_cartes_du_jour(paquet, date_jour):
    pass # à remplacer par votre code


def test_extraire_cartes_du_jour():
    c1 = Carte("Capitale de l'Italie ?", "Rome")
    c1.date_prochaine = date_future(3)
    c2 = Carte("7 x 8 ?", "56")
    c2.date_prochaine = date_future(1)
    c3 = Carte("Symbole du Fer ?", "Fe")
    c3.date_prochaine = date_future(1)
    paquet = [c1, c2, c3]
    assert extraire_cartes_du_jour(paquet, date_future(3)) == [c1, c2, c3]
    assert extraire_cartes_du_jour(paquet, date_future(1)) == [c2, c3]
    assert extraire_cartes_du_jour(paquet, date_future(0)) == []

###############################################################################
# Question 3. Fonction défaillante à analyser et corriger.                    #
###############################################################################

def extraire_cartes_a_renforcer(paquet):
    """Parcourt le paquet et renvoie la liste des cartes ayant le niveau
    d'avancement le plus faible dans le paquet."""
    if len(paquet) == 0:
        return []
        
    niveau_min = paquet[0].niveau
    a_renforcer = []
    
    for carte in paquet:
        if carte.niveau < niveau_min:
            niveau_min = carte.niveau
            a_renforcer.append(carte)
        elif carte.niveau == niveau_min:
            a_renforcer.append(carte)
            
    return a_renforcer


def test_renforcement():
    # Création de deux paquets de test
    c1 = Carte("Capitale de l'Italie ?", "Rome")
    c1.niveau = 3
    c2 = Carte("7 x 8 ?", "56")
    c2.niveau = 2
    c3 = Carte("Symbole du Fer ?", "Fe")
    c3.niveau = 4
    c4 = Carte("Symbole du Mercure ?", "Hg")
    c4.niveau = 2
    c5 = Carte("5 x 6 ?", "30")
    c5.niveau = 1
    
    mon_paquet1 = [c1, c2, c3, c4]
    mon_paquet2 = [c1, c2, c3, c4, c5]

    # Appels à la fonction défaillante
    resultat1 = extraire_cartes_a_renforcer(mon_paquet1)
    resultat2 = extraire_cartes_a_renforcer(mon_paquet2)

    # affichages test
    print("Cartes à renforcer (niveau le plus bas attendu : 2) :")
    print(resultat1)

    print("Cartes à renforcer (niveau le plus bas attendu : 1) :")
    print(resultat2)

    # tests
    assert resultat1 == [c2, c4]
    assert resultat2 == [c5]

# Question 3. Décommenter la ligne ci-dessou pour obtenir les affichages test
#test_renforcement()
