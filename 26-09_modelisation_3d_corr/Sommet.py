import math

class Sommet:

    """Représente un sommet (point) dans l'espace 3D."""

    def __init__(self, x, y, z):
        """Initialise un sommet avec ses coordonnées."""
        self.x = x
        self.y = y
        self.z = z

    def est_adjacent(self, sommet):
        """Indique si le sommet courant est adjacent à un autre sommet."""
        nb_changement = 0
        if self.x != sommet.x:
            nb_changement = nb_changement + 1
        if self.y != sommet.y:
            nb_changement = nb_changement + 1
        if self.z != sommet.z:
            nb_changement = nb_changement + 1
        return nb_changement == 1
    
    # Question 1. Écrire ici le code de la méthode distance
    def distance(self, sommet):
        carre_x = (self.x - sommet.x) ** 2
        carre_y = (self.y - sommet.y) ** 2
        carre_z = (self.z - sommet.z) ** 2
        return math.sqrt((carre_x + carre_y + carre_z))

###############################################################################
# Fonction de test pour la question 1                                         #
###############################################################################

def test_distance():
    a = Sommet(0, 0, 0)
    b = Sommet(3, 4, 0)
    c = Sommet(0, 5, 12)
    assert a.distance(b) == 5.0
    assert a.distance(c) == 13.0