from donnees import reservoirs

###############################################################################
# Question 1. Écrire et tester la fonction est_en_penurie                     #
###############################################################################

def est_en_penurie(liste_reservoirs, nom_reservoir):
    for dico in liste_reservoirs:
        if dico['nom'] == nom_reservoir:
            return dico['volume'] / dico['capacite'] < 0.2
    assert False, "réservoir absent de la liste de réservoir !"


def test_est_en_penurie():
    assert est_en_penurie(reservoirs, "Motuavai") == True
    assert est_en_penurie(reservoirs, "Nuiavai") == False

###############################################################################
# Question 2. Écrire la fonction volume_par_district                          #
###############################################################################

def volume_par_district(liste_reservoirs):
    res = {}
    for dico in liste_reservoirs:
        if dico['district'] in res:
            res[dico['district']] += dico['volume']
        else:
            res[dico['district']] = dico['volume']
    return res


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
    assert reservoirs != [], "La liste des réservoirs ne dois pas être vide !"
    somme_totale = 0
    for r in reservoirs:
        somme_totale += r["volume"]
    moyenne = somme_totale / len(reservoirs) # -1 à enlever
    return moyenne


def test_volume_moyen():
    assert volume_moyen(reservoirs) < 120000 # maximum de capacité reservoirs
    # deux premiers réservoirs de la liste ayant le même volume égal à 55000
    reservoirs_test = [reservoirs[0], reservoirs[1]]
    assert volume_moyen(reservoirs_test) == 55000

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


def ditricts_vulnerables(reservoirs, taux_alerte):
    res = []
    volume_moyen_global = volume_moyen(reservoirs)
    districts = liste_districts(reservoirs)
    dico_reservoirs_par_district = reservoirs_par_district(reservoirs)
    for district in districts:
        somme_volume = 0
        nb_reservoirs = 0
        for reservoir in dico_reservoirs_par_district[district]:
            somme_volume += reservoir['volume']
            nb_reservoirs += 1
        volume_moyen_district = somme_volume / nb_reservoirs
        if volume_moyen_district / volume_moyen_global < taux_alerte:
            res.append(district)
    return res


print(ditricts_vulnerables(reservoirs, 0.8)) # affiche ['Tepua']