###############################################################################
# Jeux de données fournis                                                     #
###############################################################################

from plantes import plantes, Plante # importantion de Plante ajoutée
from mesures import mesures

###############################################################################
# Écrire le code de la fonction croissance_moyenne de la question 1           #
###############################################################################

def croissance_moyenne(plantes: list[Plante]) -> float:
    """prend en paramètre une liste d’instances de la classe Plante et renvoie
    la moyenne des durées de croissance de l’ensemble de ces plantes (en
    jours). Si la liste fournie est vide, la fonction doit renvoyer None."""
    if plantes == []:
        # Si la liste de plantes est vide, on renvoie None.
        return None
    else:
        # Sinon, on parcourt la liste des plantes en calculant progressivement
        # la somme des durées de croissance des plantes.
        somme_durees_croissance = 0
        for p in plantes:
            somme_durees_croissance += p.croissance
        # On renvoie ensuite la moyenne en divisant cette somme par le nombre
        # de plantes.
        return somme_durees_croissance / len(plantes)


def test_croissance_moyenne():
    # Jeu de test de seulement deux plantes pour calculer la moyenne de tête
    # pour écrire le test.
    plantes_test = [
        Plante("Basilic", "Ocimum basilicum", 60, 40, "plein soleil"),
        Plante("Tomate", "Solanum lycopersicum", 80, 100, "plein soleil")
    ]
    assert croissance_moyenne(plantes_test) == 70.0
    # Cas de la liste vide
    assert croissance_moyenne([]) == None

###############################################################################
# Écrire le code de la fonction dictionnaire_mesure de la question 2          #
###############################################################################

def dictionnaire_mesure(plantes: str, mesures: list[dict]):
    dico = {}
    for nom_plante in plantes:
        liste_mesures = [m for m in mesures if m['plante'] == nom_plante]
        dico[nom_plante] = liste_mesures
    return dico


def test_dictionnaire_mesure():
    mesures_test = [
        {
            "plante": "plante1",
            "jour": 1,
            "hauteur": 100,
            "temperature": 20,
            "humidite": 100,
        },
        {
            "plante": "plante1",
            "jour": 2,
            "hauteur": 101,
            "temperature": 20,
            "humidite": 100,
        },
        {
            "plante": "plante2",
            "jour": 1,
            "hauteur": 10,
            "temperature": 20,
            "humidite": 20,
        }
    ]
    # Plantes toutes présentes dans les données
    assert dictionnaire_mesure(["plante1", "plante2"], mesures_test) == {
        "plante1": [
            {
                "plante": "plante1",
                "jour": 1,
                "hauteur": 100,
                "temperature": 20,
                "humidite": 100,
            },
            {
                "plante": "plante1",
                "jour": 2,
                "hauteur": 101,
                "temperature": 20,
                "humidite": 100,
            },
        ],
        "plante2": [
            {
                "plante": "plante2",
                "jour": 1,
                "hauteur": 10,
                "temperature": 20,
                "humidite": 20,
            }
        ],
    }
    # Une plante absente des données.
    assert dictionnaire_mesure(["plante1", "plante3"], mesures_test) == {
        "plante1": [
            {
                "plante": "plante1",
                "jour": 1,
                "hauteur": 100,
                "temperature": 20,
                "humidite": 100,
            },
            {
                "plante": "plante1",
                "jour": 2,
                "hauteur": 101,
                "temperature": 20,
                "humidite": 100,
            },
        ],
        "plante3": []
    }

###############################################################################
# Fonction défaillante à analyser et corriger pour les questions 3 et 4       #
###############################################################################

def purger_mesures_extremes(liste_mesures: list[dict]):
    """
    Supprime de la liste toutes les mesures dont la température 
    n'est pas comprise entre 20 et 25°C inclus.
    """
    # Le problème vient du fait de combiner deux actions en même temps : le
    # parcours et la suppression d'élément. Python se pert et oublie des
    # éléments.
    for mesure in liste_mesures:
        if mesure['temperature'] < 20 or mesure['temperature'] > 25:
            liste_mesures.remove(mesure)
    return liste_mesures


def purger_mesures_extremes_v2(liste_mesures: list[dict]):
    """
    Supprime de la liste toutes les mesures dont la température 
    n'est pas comprise entre 20 et 25°C inclus.
    """
    # Le problème vient du fait de combiner deux actions en même temps : le
    # parcours et la suppression d'élément. Python se pert et oublie des
    # éléments lors du parcours. Pour résoudre ce problème, on va procéder en
    # deux temps.
    # Dans un premier temps, on va lister les mesures à retirer.
    mesures_a_retirer = []
    for mesure in liste_mesures:
        if mesure['temperature'] < 20 or mesure['temperature'] > 25:
            mesures_a_retirer.append(mesure)
    # Dans un second temps on va retirer ces mesures de la liste passée
    # paramètre.
    for mesure in mesures_a_retirer:
        liste_mesures.remove(mesure)
    # Cette dernière ligne avec renvoie est inutile car la fonction est un
    # mutateur pur qui ne renvoie rien. On la désactive donc.
    #return liste_mesures


def test_purger():
    mesures_test = [
        {'jour': 1, 'plante': 'Basilic', 'temperature': 18.0},
        {'jour': 2, 'plante': 'Basilic', 'temperature': 19.0},
        {'jour': 3, 'plante': 'Basilic', 'temperature': 22.0},
        {'jour': 4, 'plante': 'Basilic', 'temperature': 28.0},
        {'jour': 5, 'plante': 'Basilic', 'temperature': 29.0}
    ]
    
    purger_mesures_extremes(mesures_test)

    print("Résultat après la purge :")
    for m in mesures_test:
        print(f"Jour {m['jour']} : {m['temperature']}°C")


def test_purger_v2():
    mesures_test = [
        {'jour': 1, 'plante': 'Basilic', 'temperature': 18.0},
        {'jour': 2, 'plante': 'Basilic', 'temperature': 19.0},
        {'jour': 3, 'plante': 'Basilic', 'temperature': 22.0},
        {'jour': 4, 'plante': 'Basilic', 'temperature': 28.0},
        {'jour': 5, 'plante': 'Basilic', 'temperature': 29.0}
    ]
    # On applique le mutateur à la liste.
    purger_mesures_extremes_v2(mesures_test)
    # On vérifie ensuite que le contenu de liste a été modifié come attendu.
    assert mesures_test == [
        {'jour': 3, 'plante': 'Basilic', 'temperature': 22.0}
    ]


if __name__ == '__main__':
    test_purger()