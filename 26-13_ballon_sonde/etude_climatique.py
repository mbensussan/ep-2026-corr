import csv

###############################################################################
# FONCTIONS DONNÉES                                                           #
###############################################################################

def recupere_donnees_fichier_csv(nom_fichier):
    """Lit des données relevées par un ballon sonde depuis un fichier CSV
    nom_fichier. Ce fichier CSV doit avoir pour descripteurs `Altitude_m`,
    `Temperature_K`, `Longitude` et `Latitude`. Renvoie les mesures d'altitude,
    de température, de longitude et de latitude dans quatre listes."""
    # Initialisation des listes de valeurs relevées
    altitudes = []                                 
    temperatures = []
    longitudes = []
    latitudes = []
    # Ouverture du fichier CSV en mode lecture.
    contenu_fichier = open(nom_fichier, 'r')
    # Suppression la 1ère ligne contannt les en-têtes des colonnes
    contenu_fichier.readline()
    # Parcours des lignes du fichier CSV contenant les donnees relevées
    for ligne in contenu_fichier.readlines():
        # rstrip() supprime les retours à la ligne ('\n') et les espaces en fin
        # de ligne
        ligne = ligne.rstrip()
        # création d'une liste de valeurs. split(";") extrait de la ligne
        # courante les valeurs qui sont délimitées par un point virgule.
        liste_valeurs = ligne.split(";")
        # conversion en entier de l'altitude et insertion dans la liste
        # correspondante
        altitudes.append(int(liste_valeurs[0]))
        # conversion en flottant de l'altitude et insertion dans la liste
        # correspondante
        temperatures.append(float(liste_valeurs[1]))
        # conversion en flotant de la température et insertion dans la liste
        # correspondante
        longitudes.append(float(liste_valeurs[2]))
        # conversion en flottant de la longitude et insertion dans la liste
        # correspondante
        latitudes.append(float(liste_valeurs[3]))
    return altitudes, temperatures, longitudes, latitudes


def genere_kml(liste_longitudes, liste_latitudes):
    """Prend en paramètre une liste de longitudes et une liste de latitudes
    correspondant aux positions successives d'un ballon sonde. Crée un fichier
    de données géographiques au format standard international KML à partir des
    données passées en paramètre. Ce fichier est visionnable ensuite dans
    différents logiciels."""
    # Création et ouverture du fichier KML en mode écriture.
    fichier_kml = open('ballon_sonde.kml', 'w')
    # Création de l'en-tête du fichier KML
    entete_fichier = '<?xml version="1.0" encoding="UTF-8"?>\n'
    entete_fichier += '<kml xmlns="http://www.opengis.net/kml/2.2">\n'
    entete_fichier += '<Document>\n'
    entete_fichier += '<name>Trajectoire ballon sonde</name>\n'
    # Écriture de l'entête dans le fichier KML
    fichier_kml.write(entete_fichier)
    # Création et écriture du reste du fichier.
    for i in range(len(liste_longitudes)):
        corps_fichier = '<Placemark>\n'
        corps_fichier += f'<name>Point {i}</name>\n'
        corps_fichier += '<Point>\n'
        corps_fichier += f'<coordinates>{liste_longitudes[i]},{liste_latitudes[i]}</coordinates>\n'
        corps_fichier += '</Point>\n'
        corps_fichier += '</Placemark>\n'
        fichier_kml.write(corps_fichier)
    bas_fichier = '</Document>\n'
    fichier_kml.write(bas_fichier)
    # Fermeture du fichier kml
    fichier_kml.close()

###############################################################################
# TRAVAIL DEMANDÉ                                                             #
###############################################################################

# QUESTION 1. Écrire votre code ci-dessous


# QUESTION 2.
def conversion_K_en_C(liste_temperatures):
    pass # à remplacer par votre code


def test_conversion_K_en_C():
    pass # à remplacer par votre test

# QUESTION 3.
def altitude_la_plus_froide(liste_altitudes, liste_temperatures):
    pass # à remplacer par votre code


def test_altitude_la_plus_froide():
    # exemple 1.
    altitudes = [7000, 10125, 13896, 14211]
    temperatures = [-35.2, -52.1, -57.4, -57.4]
    assert altitude_la_plus_froide(altitudes, temperatures) == (-57.4, [13896, 14211])
    # exemple 2.
    altitudes = [6000, 7250, 11542, 15214, 17300]
    temperatures = [-33.7, -45, -53, -58.5, -60.1]
    assert altitude_la_plus_froide(altitudes, temperatures) == (-60.1, [17300])

# QUESTION 5. Écrire votre code ci-dessous

