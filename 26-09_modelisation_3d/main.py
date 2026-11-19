from Objet3D import Objet3D
from Sommet import Sommet

###############################################################################
# Question 1. Fonction de test pour la méthode distance de la classe Sommet   #
###############################################################################

def test_distance():
    a = Sommet(0, 0, 0)
    b = Sommet(3, 4, 0)
    c = Sommet(0, 4, 5)
    # à compléter

###############################################################################
# Question 2. Fonction de test pour la méthode trouver_sommets_adjacents      #
###############################################################################

def test_trouver_sommets_adjacents():
    # test 1.
    objet1 = Objet3D()
    objet1.ajouter_sommet(2, 0, 0) # rang 0
    objet1.ajouter_sommet(1, 0, 1) # rang 1
    objet1.ajouter_sommet(1, 2, 1) # rang 2
    objet1.ajouter_sommet(0, 0, 1) # rang 3
    assert objet1.trouver_sommets_adjacents() == (objet1.sommets[1], objet1.sommets[3])
    # test 2. à compléter
    objet2 = Objet3D()

###############################################################################
# Question 3.                                                                 #
###############################################################################

parametres_imprimante = {
    'remplissage': 20,
    'vitesse_extrusion': 8 # en mm³/seconde
}


def volume_cube(cube):
    a, b = cube.sommets_adjacents()
    taille_cote = a.distance(b)  # distance donnee en mm
    return taille_cote ** 3

###############################################################################
#  Question 3. fonction estimation_impression
###############################################################################

# Écrire ci-dessous le code de la fonction estimation_impression


# Ajouter les tests ci-dessous
def test_estimation_impression():
    pass

###############################################################################
# Programme à modifier pour les questions 4 et 5                              #
###############################################################################

objet = Objet3D()
objet.ajouter_sommet(0, 0, 0)
objet.ajouter_sommet(0, 1, 0)
objet.ajouter_sommet(1, 1, 0)
objet.ajouter_sommet(1, 0, 0)
objet.ajouter_face([1, 2, 3, 4])
objet.afficher()