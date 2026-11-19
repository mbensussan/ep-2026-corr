donnees = [
    {"jour": "2025-02-04", "heure": "00:00", "chaude": 0, "froide": 1},
    {"jour": "2025-02-04", "heure": "01:00", "chaude": 0, "froide": 0},
    {"jour": "2025-02-04", "heure": "02:00", "chaude": 1, "froide": 0},
    {"jour": "2025-02-04", "heure": "03:00", "chaude": 1, "froide": 2},
    {"jour": "2025-02-04", "heure": "04:00", "chaude": 0, "froide": 0},
    {"jour": "2025-02-04", "heure": "05:00", "chaude": 1, "froide": 0},
    {"jour": "2025-02-04", "heure": "06:00", "chaude": 4, "froide": 6},
    {"jour": "2025-02-04", "heure": "07:00", "chaude": 6, "froide": 8},
    {"jour": "2025-02-04", "heure": "08:00", "chaude": 5, "froide": 8},
    {"jour": "2025-02-05", "heure": "00:00", "chaude": 0, "froide": 1},
    {"jour": "2025-02-05", "heure": "01:00", "chaude": 0, "froide": 0},
    {"jour": "2025-02-05", "heure": "02:00", "chaude": 1, "froide": 1},
    {"jour": "2025-02-05", "heure": "03:00", "chaude": 0, "froide": 1},
    {"jour": "2025-02-05", "heure": "04:00", "chaude": 2, "froide": 1},
    {"jour": "2025-02-05", "heure": "05:00", "chaude": 0, "froide": 0},
]

###############################################################################
# Question 1. Fonction à compléter et à tester                                #
###############################################################################

def consos_jour(donnees, jour):
    """Renvoie la consommation totale d’eau (somme de l’eau chaude et de l’eau
    froide) de toutes les mesures des données pour le jour passé en paramètre.
    """
    res = [] # liste résultat au départ vide
    # On parcourt la liste des mesures.
    for mesure in donnees:
        # Si on rencontre une mesure du jour passé en paramètre,
        if mesure["jour"] == jour:
            # on ajoute à la liste résultat la somme des consommations d'eau
            # chaude et froide de l'heure.
            res.append(mesure["chaude"] + mesure["froide"])
    # à l'issue du parcours,
    if res == []:
        # si la liste résultat est vide, cela signifie qu'il n'y pas de mesures
        # pour ce jour et on renvoie None.
        return None
    else:
        # Sinon, on renvoie la liste résultat.
        return res


def test_consos_jour():
    assert consos_jour(donnees, "2025-02-04") == [1, 0, 1, 3, 0, 1, 10, 14, 13]
    assert consos_jour(donnees, "2025-02-05") == [1, 0, 2, 1, 3, 0]
    assert consos_jour(donnees, "2025-12-25") == None

###############################################################################
# Question 2. Fonction à compléter et à tester                                #
###############################################################################

def fuite_possible(donnees, jour):
    # On récupère la liste des consommations totales du jour par heure.
    consos = consos_jour(donnees, jour)
    consos_positives_consecutives = 0 # variable compteur
    # On parcourt les cinq premiers éléments de la liste (de 00:00 à 05:00)
    # tant que l'on a pas dépassé 3 mesures positives consécutives.
    i = 0
    while i < 6 and consos_positives_consecutives < 3:
        if consos[i] > 0:
            # si on rencontre une valeur positive, on incrémente le compteur
            consos_positives_consecutives += 1
        else:
            # dans le cas contraire on remet à zéro le compteur
            consos_positives_consecutives = 0
        i += 1
    # Deux scénarios possibles :
    # 1. La boucle s'arrête dès que l'on a trouvée 3 valeurs consécutives. Cela
    # évite de continuer le parcours et risquer de remettre à zéro le compteur
    # aux étapes suivantes.
    # 2. On termine le parcours sans trouver 3 valeurs consécutives.
    # Le dernier tests ci-dessous permet de distinguer ces deux scénarios.
    return consos_positives_consecutives >= 3

# autre version avec une boucle for

def fuite_possible2(donnees, jour):
    # On récupère la liste des consommations totales du jour par heure.
    consos = consos_jour(donnees, jour)
    consos_positives_consecutives = 0 # variable compteur
    # On parcours les cinq premiers éléments de la liste (de 00:00 à 05:00)
    # tant que l'on a pas dépassé 3 mesures positives consécutives.
    for i in range(6):
        if consos[i] > 0:
            # si on rencontre une valeur positive, on incrémente le compteur
            consos_positives_consecutives += 1
        else:
            # dans le cas contraire on remet à zéro le compteur
            consos_positives_consecutives = 0
        if consos_positives_consecutives == 3:
            # En fin d'itération, si on a atteint 3 mesures positives
            # consécutives, on renvoie True
            return True
    # Si la boucle se termine, cela signifie l'on a pas trouvé 3 mesures
    # consécutives positives et on revoie donc False.
    return False

def test_fuite_possible():
    assert fuite_possible(donnees, "2025-02-04") == False
    assert fuite_possible(donnees, "2025-02-05") == True

def test_fuite_possible2():
    assert fuite_possible2(donnees, "2025-02-04") == False
    assert fuite_possible2(donnees, "2025-02-05") == True

###############################################################################
# Question 3 et 4. Fonction fournie (erronée) à tester et corriger            #
###############################################################################

def lissage_conso(valeurs):
    """Calcule une moyenne glissante sur les valeurs. Pour chaque valeur, on
    calcule la moyenne avec ses voisins."""
    # Question 4. branchement supplémentaire ajouté ###########################
    if len(valeurs) < 2: # liste vide ou à un seul élément
        return valeurs
    ###########################################################################
    lisse = []
    for i in range(len(valeurs)):
        if i == 0:
            m = (valeurs[i] + valeurs[i+1]) / 2
        elif i == len(valeurs) - 1:
            m = (valeurs[i-1] + valeurs[i]) / 2
        else:
            # Question 3. il fallait remplacer ci-dessous le 2 par 3.
            m = (valeurs[i-1] + valeurs[i] + valeurs[i+1]) / 3
        lisse.append(m)
    return lisse


def test_lissage():
    # Question 3. Test fourni à utiliser
    assert lissage_conso([10, 20, 30, 40, 50]) == [15.0, 20.0, 30.0, 40.0, 45.0]
    # Question 4. Tests supplémentaires à écrire ci-dessous
    assert lissage_conso([10, 20]) == [15, 15]
    # Cas limite non pris en charge au départ : liste est vide ou à un seul
    # élément une possibilité est de renvoyer la liste inchangée.
    # Pour l'instant une erreur d'indice est déclenchée puisque la fonction
    # essai d'accéder à des cases voisines qui n'existent pas.
    assert lissage_conso([]) == []
    assert lissage_conso([10]) == [10]