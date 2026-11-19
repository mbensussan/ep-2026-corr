from math import sqrt
#from donnees_habitats_original_foireux import zones_connues
from donnees_habitats import zones_connues

###############################################################################
# Question 1.                                                                 #
###############################################################################

def distance(habitat_1, habitat_2):
    """Calcule la distance euclidienne entre deux habitats.
    Prend en paramètres : 
        - habitat_1 : dictionnaire représentant un habitat.
        - habitat_2 : dictionnaire représentant un autre habitat.
    Renvoie : 
        - float : distance euclidienne entre habitat_1 et habitat_2.
    """
    # On accumule les différences au carré.
    somme_carres = 0
    for cle in habitat_1:
        somme_carres += (habitat_1[cle] - habitat_2[cle]) ** 2
    # On renvoie ensuite la racine carrée de cette somme.
    return sqrt(somme_carres)


def test_distance():
    assert distance(zones_connues[0], zones_connues[1]) == 10.954451150103322
    assert distance(zones_connues[0], zones_connues[2]) == 2.8284271247461903
     
###############################################################################
# Question 2.                                                                 #
###############################################################################

def distance_d_un_habitat(habitat, habitats):
    """Calcule la distance entre un habitat et chaque habitat de la liste.
    Prend en paramètres : 
        - habitat : dictionnaire représentant un habitat.
        - habitats : liste de dictionnaires représentant des habitats.
    Renvoie : 
        - list[tuple] : liste de tuples (distance, habitat) où distance est la
        distance entre habitat et chaque habitat de la liste.
    """
    return [(distance(habitat, h), h) for h in habitats]
    

def test_distance_d_un_habitat():
    habitat_test = {'vegetation': 5, 'proximite_eau': 2, 'densite_urbaine': 4, 'disponibilite_proies': 6}
    zones_test = zones_connues[:3] # trois premiers habitats des données
    assert distance_d_un_habitat(habitat_test, zones_test) == [
        (7.211102550927978, {'vegetation': 9, 'proximite_eau': 6, 'densite_urbaine': 0, 'disponibilite_proies': 4, 'presence_renard': 0}),
        (8.660254037844387, {'vegetation': 10, 'proximite_eau': 5, 'densite_urbaine': 9, 'disponibilite_proies': 10, 'presence_renard': 1}),
        (5.196152422706632, {'vegetation': 8, 'proximite_eau': 5, 'densite_urbaine': 1, 'disponibilite_proies': 6, 'presence_renard': 1})
    ]

###############################################################################
# Questions 3. et 4.                                                          #
###############################################################################

def k_plus_proches(k, habitat, habitats):
    """Identifie les k habitats les plus proches de l'habitat donné.
    Prend en paramètre : 
        - k : entier représentant le nombre d'habitats à renvoyer.
        - habitat : dictionnaire représentant un habitat.
        - habitats : liste de dictionnaires représentant des habitats.
    Renvoie : 
        - list[tuple] : liste de tuples (distance, habitat) où distance est la
        distance entre habitat et chaque habitat sélectionné.
    """
    # On crée la liste de tuples (distance, habitat).
    distances = distance_d_un_habitat(habitat, habitats)
    # On trie la liste de tuples par distance euclidienne croissante.
    distances.sort(key = lambda x: x[0])
    # On renvoie les k premiers éléments de la liste triée.
    return distances[:k]


def presence_renard(k, habitat, habitats):
    """Vérifie si l'habitat donné a plus de k/2 voisins avec des renards.
    Prend en paramètre : 
        - k : entier représentant le nombre d'habitats voisins à considérer.
        - habitat : dictionnaire représentant un habitat.
        - habitats : liste de dictionnaires représentant des habitats.
    Renvoie : 
        - bool : True si l'habitat a plus de k/2 voisins avec des renards,
        False sinon.
    """
    voisins = k_plus_proches(k, habitat, habitats)
    n_renards = 0
    for voisin in voisins:
        # Question 3. Voisin est en fait un tuple de type (distance, habitat)
        # Il faut accéder à son second élément qui est le dictionnaire
        # contenant la clé 'presence_renard'. On peut procéder par exemple par
        # unpacking :
        distance, habitat = voisin
        # On pouvait aussi utiliser l'indiçage : habitat = voisin[0]
        if habitat['presence_renard'] == 1:
            n_renards += 1
    return n_renards > k / 2


zone_inconnue = {'vegetation': 6, 'proximite_eau': 4, 'densite_urbaine': 3, 'disponibilite_proies': 6}

if __name__ == '__main__':
    # Question 3. Compléter le programme ci-dessous
    print(presence_renard(3, zone_inconnue, zones_connues))

    # Question 4. Compléter le programme ci-dessous
    # On affiche le résultat pour k allant de 1 à 30
    # Pour k = 1 et k = 3, on obtient False (absence de renards) et les autres
    # k testés on obtient True (présence de renard). Cela montre qu'il faut
    # choisir un k suffisemment grand pour éviter d'obtenir un résultat
    # non représentatif. Remarque. L'habitat inconnu choisi est clairement
    # dans le nuage de point des habitats avec renards hors de la zone de
    # chevauchement avec le nuage des habitats sans renards. Si on avait choisi
    # un habitat inconnu proche de la zone de chevauchement, choisir une
    # valeur de k trop élevée aurait également été problématique (dans les
    # données générées, il y a une majorité (environ 2/3) d'habitats sans
    # renard.)
    for k in range(1, 31):
        print(f'k: {k} \t Présence renards : {presence_renard(k, zone_inconnue, zones_connues)}')