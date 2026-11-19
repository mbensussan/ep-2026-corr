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
    # À compléter
    pass


def test_consos_jour():
    assert consos_jour(donnees, "2025-02-04") == [1, 0, 1, 3, 0, 1, 10, 14, 13]
    assert consos_jour(donnees, "2025-02-05") == [1, 0, 2, 1, 3, 0]
    assert consos_jour(donnees, "2025-12-25") == None

###############################################################################
# Question 2. Fonction à compléter et à tester                                #
###############################################################################

def fuite_possible(donnees, jour):
    # À compléter
    pass


def test_fuite_possible():
    assert fuite_possible(donnees, "2025-02-04") == False
    assert fuite_possible(donnees, "2025-02-05") == True

###############################################################################
# Question 3 et 4. Fonction fournie (erronée) à tester et corriger            #
###############################################################################

def lissage_conso(valeurs):
    """Calcule une moyenne glissante sur les valeurs. Pour chaque valeur, on
    calcule la moyenne avec ses voisins."""
    lisse = []
    for i in range(len(valeurs)):
        if i == 0:
            m = (valeurs[i] + valeurs[i+1]) / 2
        elif i == len(valeurs) - 1:
            m = (valeurs[i-1] + valeurs[i]) / 2
        else:
            m = (valeurs[i-1] + valeurs[i] + valeurs[i+1]) / 2
        lisse.append(m)
    return lisse


def test_lissage():
    # Question 3. Test fourni à utiliser
    assert lissage_conso([10, 20, 30, 40, 50]) == [15.0, 20.0, 30.0, 40.0, 45.0]
    # Question 4. Tests supplémentaires à écrire ci-dessous
