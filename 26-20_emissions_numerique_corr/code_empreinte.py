# Données d'émissions en gCO2e par unité
EMISSIONS = {
    'emails_simples': 4,       # par email
    'emails_pj': 19,           # par email avec pièce jointe
    'streaming_sd': 36,        # par heure
    'streaming_hd': 100,       # par heure
    'recherches': 7,           # par recherche
    'stockage_cloud': 10       # par Go par mois
}

# Exemples d'utilisateurs pour les tests

utilisateur1 = {
    'emails_simples': 150,
    'emails_pj': 20,
    'streaming_sd': 10,
    'streaming_hd': 25,
    'recherches': 500,
    'stockage_cloud': 15
}

utilisateur2 = {
    'streaming_hd': 15,
    'emails_simples': 100,
    'recherches': 10
}

utilisateur3 = {
    'emails_simples': 50,
    'emails_pj': 5,
    'streaming_sd': 30,
    'streaming_hd': 5,
    'recherches': 200,
    'stockage_cloud': 5
}

utilisateur4 = {
    'emails_simples': 100,
    'recherches': 50
}

utilisateur5 = {
    'emails_simples': 50,
    'recherches': 100
}

utilisateur6 = {
    'emails_simples': 75,
    'stockage_cloud': 5
}

utilisateur7 = {}



###############################################################################
# Question 1. Écrire le code de la fonction calculer_empreinte et la tester   #
###############################################################################

def calculer_empreinte(utilisateur):
    res = 0
    for activite in utilisateur:
        res += utilisateur[activite] * EMISSIONS[activite]
    return res


def test_calculer_empreinte():
    assert calculer_empreinte(utilisateur1) == 7490

###############################################################################
# Question 2. Écrire le code de la fonction classer_par_impact et la tester   #
###############################################################################

def classer_par_impact(utilisateur):
    dico = {
        "fort": [],
        "moyen": [],
        "faible": []
    }
    for activite in utilisateur:
        emissions = utilisateur[activite] * EMISSIONS[activite]
        if emissions >= 1000:
            dico["fort"].append(activite)
        elif emissions >= 200:
            dico["moyen"].append(activite)
        else:
            dico["faible"].append(activite)


def test_classer_par_impact():
    classer_par_impact(utilisateur2) == {
        'fort': ['streaming_hd'],
        'moyen': ['emails_simples'],
        'faible': ['recherches']
    }

###############################################################################
# Question 3. Compléter les tests pour tester la fonction comparer            #
###############################################################################

def comparer(u1, u2):
    """Compare les émissions de deux utilisateurs pour toutes les activités.
    Renvoie un dictionnaire avec, pour chaque activité, la différence des
    émissions (émissions de l’utilisateur 2 moins celles de l’utilisateur 1).
    Si une activité est absente chez un utilisateur, on considère que
    son émission vaut 0."""
    differences = {}
    for activite in EMISSIONS:
        quantite1 = 0
        quantite2 = 0
        if activite in u1:
            quantite1 = u1[activite]
        if activite in u2:
            quantite2 = u2[activite]
        emission1 = quantite1 * EMISSIONS[activite]
        emission2 = quantite2 * EMISSIONS[activite]
        differences[activite] = emission2 - emission1
    return differences


def test_comparer():
    # Utilisateurs différents avec les mêmes activités
    diff = comparer(utilisateur4, utilisateur5)
    assert diff['emails_simples'] == -200  # (50-100) * 4
    assert diff['recherches'] == 350     # (100-50) * 7
    # Utilisateurs identiques
    assert comparer(utilisateur4, utilisateur4) == {
        'emails_pj': 0,
        'emails_simples': 0,
        'recherches': 0,
        'stockage_cloud': 0,
        'streaming_hd': 0,
        'streaming_sd': 0,
    }
    # Premier utilisateur vide
    assert comparer(utilisateur7, utilisateur5) == {
        'emails_pj': 0,
        'emails_simples': 200, # 50 * 4
        'recherches': 700, # 100 * 7
        'stockage_cloud': 0,
        'streaming_hd': 0,
        'streaming_sd': 0,
    }
    # Utilisateurs n'ayant pas toutes les activités dont une en commun et
    # deux différentes.
    assert comparer(utilisateur5, utilisateur6) == {
        'emails_pj': 0, # aucun des deux ne la pratique
        'emails_simples': 100, # (75 - 50) * 4) u1 et u2 la pratiquent
        'recherches': -700, # (0 - 100) * 7) u1 la pratique et u2 non
        'stockage_cloud': 50, # (5 - 0) * 10 u1 ne la pratique pas et u2 oui
        'streaming_hd': 0, # aucun des deux ne la pratique
        'streaming_sd': 0 # aucun des deux ne la pratique
    }


###############################################################################
# Question 4. Tester et corriger la fonction comparer_v2                      #
###############################################################################

def comparer_v2(u1, u2):
    """Compare les émissions de deux utilisateurs pour toutes les activités.
    Renvoie un dictionnaire avec, pour chaque activité, l'écart des émissions
    sous forme de pourcentage, en proportion de la première émission."""
    ecarts = {}
    for activite in EMISSIONS:
        quantite1 = 0
        quantite2 = 0
        if activite in u1:
            quantite1 = u1[activite]
        if activite in u2:
            quantite2 = u2[activite]
        emission1 = quantite1 * EMISSIONS[activite]
        emission2 = quantite2 * EMISSIONS[activite]
        # branchement conditionnel ajouté ci-dessous
        if emission1 == 0: # si u1 ne pratique pas l'activité
            if emission2 == 0: # si u2 ne pratique pas non plus l'activité
                ecarts[activite] = 0.0 # aucun écart
            else: # par contre si u2 pratique l'activité
                ecarts[activite] = 100.0
        else: # emission1 est différent de zéro, on peut appliquer la formule
            ecarts[activite] = (emission2 - emission1)/emission1 * 100
    return ecarts


def test_comparer_v2():
    # Cas 1. u1 pratique toutes les activités. Aucun problème car la variable
    # emission1 au dénominateur de la formule ne s'annule jamais.
    comparer_v2(utilisateur1, utilisateur2) == {
        'emails_pj': -100.0,
        'emails_simples': -33.33333333333333,
        'recherches': -98.0,
        'stockage_cloud': -100.0,
        'streaming_hd': -40.0,
        'streaming_sd': -100.0
    }
    # Cas 2. u1 n'a qu'une partie des activités. Pour les activité pratiquées
    # par u1 la formule fonctionne par contre pour les activités non pratiquées
    # par u1 il y a déclenchement d'une ZeroDivisionError car dans le calcul
    # emission1 est au dénominateur et ne peut pas être nul. Dans ce cas où u1
    # ne pratique pas l'activité, il faut éviter le calcul et choisir :
    # - la valeur 100.0 (100%) si u2 pratique l'activité ;
    # - la valeur 0.0 (0%) si u2 ne la pratique pas non plus (aucun écart
    # entre u1 et u2)
    # Voir le branchement conditionnel ajouté dans la fonction comparer_v2
    assert comparer_v2(utilisateur5, utilisateur6) == {
        'emails_pj': 0.0, # aucun des deux ne la pratique
        'emails_simples': 50.0, # (75 - 50) / 50 = 50% u1 et u2 la pratiquent
        'recherches': -100.0, # u1 la pratique et u2 ne la pratique pas
        'stockage_cloud': 100.0, # u1 ne la pratique pas et u2 la pratique
        'streaming_hd': 0.0, # aucun des deux ne la pratique
        'streaming_sd': 0.0 # aucun des deux ne la pratique
    }