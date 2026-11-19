import sqlite3

###############################################################################
# Question 1. Nettoyage des numéros de téléphone                              #
###############################################################################

def normalisation_tel(tel):
    res = ''
    for car in tel:
        if car.isdigit():
            res += car
    return res


def test_normalisation_tel():
    assert normalisation_tel("06 12 99 90 12") == "0612999012"
    assert normalisation_tel("02 12 99 90 12") == "0212999012"
    assert normalisation_tel("02.12.99.90.12") == "0212999012"
    assert normalisation_tel("0.6.12.99.90.12") == "0612999012"
    assert normalisation_tel("06-12-99-90-12") == "0612999012"
    assert normalisation_tel("(0)6.12.99-90-12 gilbert") == "0612999012"
    assert normalisation_tel("061299901") == "061299901"
    assert normalisation_tel("06129990123") == "06129990123"
    print('Les tests de la fonction normalisation_tel sont passés')

###############################################################################
# Question 2. Validation des numéros de téléphone                             #
###############################################################################

def validation_tel(tel):
    """Validation des numéros de téléphone portable français selon les
    conditions spécifiées.

    Prend en paramètre :
        tel (str) : numéro de téléphone nettoyé
    Renvoie (bool) :
        True si le numéro est valide, False sinon
    """
    if len(tel) != 10:
        return False
    if tel[0] != "0":
        return False
    if tel[1] != "6" and tel[1] != "7":
        return False
    return True


def test_validation_tel():
    # Il s'agit de tests de couverture qui doivent traiter tous les cas pris
    # en charge par le branchement conditionnel de la fonction.
    # 1. numéros de téléphone corrects
    assert validation_tel('0612345678') == True
    assert validation_tel('0712345678') == True
    # Dans la suite pour chaque test, tout doit être correct sauf le point
    # testé.
    # 2. longueur du téléphone incorrecte
    assert validation_tel('06123456') == False # trop court
    assert validation_tel('061234567890') == False # trop long
    # 3. le premier chiffre du téléphone n'est pas zéro
    assert validation_tel('1612345678') == False
    assert validation_tel('1712345678') == False
    # 4. le second chiffre du téléphone n'est ni 6 ni 7
    assert validation_tel('0012345678') == False


###############################################################################
# Question 3. Détermination de la liste des chats à vacciner (interrogation   #
# de la base de données)                                                      #
###############################################################################

DB_PATH = "cabinet.sqlite"

def proprietaires_animaux_nes_apres(date):
    """Renvoie dans une liste de tuple les noms et prénoms des propriétaires
    d'animaux nés après la date `date`, triés par ordre alphabétique de noms
    puis prénoms.

    Prend en paramètre :
        date (str) : date de naissance minimale
    Renvoie (liste[tuple]) :
        liste de tuples de la forme (nom_proprietaire, prenom_proprietaire)
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    resultat = cursor.execute(
        """
        SELECT proprietaire.nom, proprietaire.prenom
        FROM proprietaire
            JOIN animal ON proprietaire.id = animal.id_proprietaire 
        WHERE animal.date_naissance > ?
        ORDER BY proprietaire.nom, proprietaire.prenom;
        """,
        (date,)
    )
    return list(resultat)


def consultation_vaccination_chat(date):
    """Renvoie les consultations de vaccination de chats dont la date est
    supérieure à la date `date`.

    Prend en paramètre :
        date (str) : date minimale
    Renvoie (liste[tuple]) : 
        liste de tuples de la forme 
        (id_animal, nom_animal, tel_proprietaire, date_consultation)
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    resultat = cursor.execute(
        """
        SELECT animal.id, animal.nom, proprietaire.telephone, consultation.date
        FROM proprietaire
            JOIN animal ON proprietaire.id = animal.id_proprietaire
            JOIN consultation ON consultation.id_animal = animal.id
        WHERE consultation.date > ? AND consultation.motif = "vaccination"
        AND espece = "chat"
        ORDER BY animal.id, consultation.date;
        """,
        (date,)
    )
    # piège : il ne famait pas oublier de filtrer le motif de consultation et
    # l'espèce !
    return list(resultat)


def test_consultation_vaccination_chat():
    vaccinations = consultation_vaccination_chat("20240923")
    assert len(vaccinations) == 118
    assert vaccinations[0] == (16,  "Plume",  "0.6.36.96.89.83", "20241024")
    assert vaccinations[1] == (16,  "Plume",  "0.6.36.96.89.83", "20251125")
    assert vaccinations[2] == (17, "Gollum",  "0.6.36.96.89.83", "20250113")
    assert vaccinations[3] == (26, "Olympe", "(0)4 73 98 01 23", "20250109")
    assert vaccinations[4] == (32, "Chopin",   "06.37.97.66.64", "20241201")
    assert vaccinations[5] == (32, "Chopin",   "06.37.97.66.64", "20251119")
    assert vaccinations[6] == (34,   "Jazz",  "0.6.37.51.65.52", "20250801")
    assert vaccinations[7] == (35,  "Tango",          "0324182", "20250706")
    assert vaccinations[8] == (38, "Loulou",   "05-35-95-87-54", "20250209")
    print('Les tests de la fonction consultation_vaccination_chat sont passés')

###############################################################################
# Question 4. Détermination de la date de dernière vaccination                #
###############################################################################

def derniere_vaccination(consultations):
    """Renvoie un dictionnaire ayant pour clef l'identifiant de l'animal,
    et dont la valeur associée est la dernière consultation de cet animal.

    Chaque consultation est un tuple de la forme :
    (id_animal, nom_animal, tel_proprietaire, date_consultation)
    """
    derniere = {}
    for consult in consultations:
        id_animal = consult[0]
        date = consult[3]
        if id_animal not in derniere:
            derniere[id_animal] = consult
        elif date > derniere[id_animal][3]: # l'ordre devait être inversé
            # L'étape de mise à jour du minimum avait été oubliée
            date = derniere[id_animal][3] # cette ligne devait être ajoutée
            derniere[id_animal] = consult
    return derniere


def test_derniere_vaccination():
    consultations_pour_test = [
        (16,  "Plume",  "0.6.36.96.89.83", "20241024"),
        (16,  "Plume",  "0.6.36.96.89.83", "20251125"),
        (17, "Gollum",  "0.6.36.96.89.83", "20250113"),
        (26, "Olympe", "(0)4 73 98 01 23", "20250109"),
        (32, "Chopin",   "06.37.97.66.64", "20241201"),
        (32, "Chopin",   "06.37.97.66.64", "20251119"),
        (34,   "Jazz",  "0.6.37.51.65.52", "20250801"),
        (35,  "Tango",          "0324182", "20250706"),
        (38, "Loulou",   "05-35-95-87-54", "20250209"),
        (39,  "Tango",   "07.45.48.02.42", "20250329"),
        (40, "Sésame",   "07.45.48.02.42", "20250228"),
        (41,  "Pixel",       "0130709285", "20241204"),
        (41,  "Pixel",       "0130709285", "20251222"),
    ]

    resultat = derniere_vaccination(consultations_pour_test)
    # Affichage des résultats, décommenter si besoin les deux lignes ci-dessous
    # for a, r in resultat.items():
    #     print(a, ":", r)

    assert derniere_vaccination(consultations_pour_test) == {
        16: (16,  "Plume",  "0.6.36.96.89.83", "20251125"),
        17: (17, "Gollum",  "0.6.36.96.89.83", "20250113"),
        26: (26, "Olympe", "(0)4 73 98 01 23", "20250109"),
        32: (32, "Chopin",   "06.37.97.66.64", "20251119"),
        34: (34,   "Jazz",  "0.6.37.51.65.52", "20250801"),
        35: (35,  "Tango",          "0324182", "20250706"),
        38: (38, "Loulou",   "05-35-95-87-54", "20250209"),
        39: (39,  "Tango",   "07.45.48.02.42", "20250329"),
        40: (40, "Sésame",   "07.45.48.02.42", "20250228"),
        41: (41,  "Pixel",       "0130709285", "20251222"),
    }
    print('Les tests de la fonction derniere_vaccination sont passés')
