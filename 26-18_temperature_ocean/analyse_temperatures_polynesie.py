###############################################################################
# Question 1. Écrire le code de la fonction temperature_moyenne et la tester  #
###############################################################################

# Données de test pour la questions 1.
donnees_test1 = [
    {'date': '2020-01-15', 'zone': 'Societe', 'temperature': 28.5},
    {'date': '2020-01-16', 'zone': 'Societe', 'temperature': 29.0},
    {'date': '2020-01-15', 'zone': 'Tuamotu', 'temperature': 27.5}
]

def temperature_moyenne(zone, donnees):
    pass # à remplacer par votre code


def test_temperature_moyenne():
    assert temperature_moyenne('Societe', donnees_test1) == 28.75
    assert temperature_moyenne('Tuamotu', donnees_test1) == 27.5
    assert temperature_moyenne('Marquises', donnees_test1) == None

###############################################################################
# Question 2 : Écrire le code de la fonction detection_anomalies et la tester #
###############################################################################

# Données de test pour la question 2.
donnees_test2 = [
    {'date': '2020-01-15', 'zone': 'Societe', 'temperature': 28.5},
    {'date': '2020-01-16', 'zone': 'Societe', 'temperature': 33.0},
    {'date': '2020-01-17', 'zone': 'Societe', 'temperature': 29.0},
    {'date': '2020-01-18', 'zone': 'Societe', 'temperature': 29.0},
    {'date': '2020-01-19', 'zone': 'Societe', 'temperature': 32.5},
    {'date': '2020-01-15', 'zone': 'Tuamotu', 'temperature': 27.5},
    {'date': '2020-01-16', 'zone': 'Tuamotu', 'temperature': 28.5}
]

def detecter_anomalies(zone, seuil, donnees):
    pass # à remplacer par votre code


def test_detecter_anomalies():
    detecter_anomalies('Societe', 3.0, donnees_test2) == ['2020-01-16', '2020-01-19']
    detecter_anomalies('Societe', 5.0, donnees_test2) == []
    detecter_anomalies('Marquises', 1.0, donnees_test2) == []

###############################################################################
# Question 3. et 4. fonction evolution_par_decennie à tester puis corriger    #
###############################################################################

def evolution_par_decennie(zone, donnees):
    """Calcule l'évolution des températures moyennes par décennie pour une
    zone.

    ATTENTION: Cette fonction contient un bug volontaire à détecter et
    corriger.

    Prend en paramètre:
        zone (str): Nom de l'archipel (ex: 'Societe', 'Tuamotu')
        donnees (list): Liste de dictionnaires de relevés

    Renvoie (dict):
        Dictionnaire {décennie : température_moyenne}
            ex: {2010: 27.5, 2020: 28.3}
        Renvoie un dictionnaire vide si la zone n'existe pas.
    """
    # Filtrage des relevés pour la zone
    releves_zone = [r for r in donnees if r['zone'] == zone]

    if releves_zone == []:
        return {}

    # Regroupement par décennie
    temperatures_par_decennie = {}

    for releve in releves_zone:
        # Extraction de l'année de la date (format: 'YYYY-MM-DD')
        annee = int(releve['date'].split('-')[0])

        # Calcul de la décennie
        decennie = (annee // 10)

        if decennie not in temperatures_par_decennie:
            temperatures_par_decennie[decennie] = []

        temperatures_par_decennie[decennie].append(releve['temperature'])

    # Calcul des moyennes
    moyennes = {}
    for decennie, temperatures in temperatures_par_decennie.items():
        moyennes[decennie] = round(sum(temperatures) / len(temperatures), 2)

    return moyennes


# Données de test pour les questions 3. et 4.
donnees_test3 = [
    # Société - Données sur 2010 et 2020
    {'date': '2010-01-15', 'zone': 'Societe', 'temperature': 27.0},
    {'date': '2010-06-20', 'zone': 'Societe', 'temperature': 26.5},
    {'date': '2011-03-10', 'zone': 'Societe', 'temperature': 27.5},
    {'date': '2020-02-14', 'zone': 'Societe', 'temperature': 28.0},
    {'date': '2020-08-22', 'zone': 'Societe', 'temperature': 28.5},
    {'date': '2021-05-30', 'zone': 'Societe', 'temperature': 29.0},

    # Tuamotu - Données sur 2010 et 2020
    {'date': '2015-04-10', 'zone': 'Tuamotu', 'temperature': 26.8},
    {'date': '2020-07-15', 'zone': 'Tuamotu', 'temperature': 27.0},
    {'date': '2021-09-20', 'zone': 'Tuamotu', 'temperature': 29.0},


    # Marquises - Données uniquement sur 2020
    {'date': '2020-03-15', 'zone': 'Marquises', 'temperature': 25.5},
    {'date': '2021-07-10', 'zone': 'Marquises', 'temperature': 26.0},
    {'date': '2022-11-25', 'zone': 'Marquises', 'temperature': 26.5},
]

# Question 3. Test à compléter
def test_zone_inexistante():
    """Test 1 : Tester une zone qui n'existe pas

    À compléter:
    1. Appeler evolution_par_decennie avec une zone inexistante
    2. Vérifier que le résultat est un dictionnaire vide
    """
    pass  # à remplacer par votre code


# Question 3. Test à compléter
def test_une_seule_decennie():
    """Test 2: Tester une zone avec données sur une seule décennie

    À compléter:
    1. Appeler evolution_par_decennie avec la zone appropriée
    2. Vérifier que le résultat ne contient qu'une seule décennie (2020)
    3. Vérifier la température moyenne
    """
    pass  # à remplacer par votre code


# Question 3. Test à compléter
def test_plusieurs_decennies():
    """Test 3 : Tester une zone avec données sur plusieurs décennies

    À compléter:
    1. Appeler evolution_par_decennie avec la zone appropriée
    2. Vérifier que le résultat contient bien les clés 2010 et 2020
    3. Vérifier que les températures moyennes sont cohérentes
    """
    pass  # à remplacer par votre code