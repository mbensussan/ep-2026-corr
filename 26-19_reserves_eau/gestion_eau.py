from donnees import reservoirs

###############################################################################
# Question 1. Écrire et tester la fonction est_en_penurie                     #
###############################################################################

def est_en_penurie(liste_reservoirs, nom_reservoir):
    pass # à remplacer par votre code


def test_est_en_penurie():
    assert est_en_penurie(reservoirs, "Motuavai") == True
    assert est_en_penurie(reservoirs, "Nuiavai") == False

###############################################################################
# Question 2. Écrire la fonction volume_par_district                          #
###############################################################################

def volume_par_district(liste_reservoirs):
    pass # à remplacer par votre code


def test_volume_par_district():
    assert volume_par_district(reservoirs) == {
        'Tepua':    90000,
        'Fare':    170000,
        'Hiva Oro': 90000,
        'Avera':   130000
    }

###############################################################################
# Question 3. Écriture de tests et correction de la fonction volume_moyen     #
###############################################################################

def volume_moyen(reservoirs):
    """Renvoie le volume moyen d'eau disponible dans les réservoirs."""
    somme_totale = 0
    for r in reservoirs:
        somme_totale += r["volume"]
    moyenne = somme_totale / (len(reservoirs)-1)
    return moyenne


def test_volume_moyen():
    pass # à remplacer par vos tests

###############################################################################
# Question 4. Identification des dictricts vulnérables                        #
###############################################################################

def liste_districts(reservoirs):
    """Renvoie la liste des districts présents dans les données."""
    liste = []
    for r in reservoirs:
        if (r["district"] not in liste):
            liste.append(r["district"])
    return liste


def reservoirs_par_district(reservoirs):
    """Renvoie un dictionnaire associant chaque district à la liste des
    réservoirs qui s’y trouvent.
    """
    liste_rpd = {}
    for r in reservoirs:
        district = r["district"]
        if district not in liste_rpd:
            liste_rpd[district] = []
        liste_rpd[district].append(r)
    return liste_rpd


# Question 4. Ajouter votre code ci-dessous.