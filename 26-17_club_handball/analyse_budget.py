import csv

def lire_mouvements_depuis_csv(nom_fichier_csv):
    """Lit des mouvement d'un fichier CSV et les renvoie dans une liste de
    dictionnaires. Les colonnes 'montant' et 'mois' sont converties
    respectivement en flottant et en entier."""
    mouvements_csv = []
    try:
        with open(nom_fichier_csv, mode='r', newline='', encoding='utf-8') as fichier_csv:
            lecteur_csv = csv.DictReader(fichier_csv)
            for ligne in lecteur_csv:
                ligne['montant'] = float(ligne['montant'])
                ligne['mois'] = int(ligne['mois'])
                mouvements_csv.append(ligne)
        return mouvements_csv
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{nom_fichier_csv}' est introuvable.")
        return []


# Jeux de données

mouvements_complets = lire_mouvements_depuis_csv("budget_complet.csv")

mouvements_test = [
    {'type': 'recette', 'catégorie': 'cotisations', 'montant': 1200.0, 'mois': 1},
    {'type': 'recette', 'catégorie': 'billetterie', 'montant': 300.0, 'mois': 6},
    {'type': 'dépense', 'catégorie': 'fonctionnement', 'montant': 450.0, 'mois': 6},
    {'type': 'dépense', 'catégorie': 'déplacements', 'montant': 200.0, 'mois': 12},
    {'type': 'dépense', 'catégorie': 'salaires', 'montant': 1500.0, 'mois': 12},
    {'type': 'recette', 'catégorie': 'subventions', 'montant': 800.0, 'mois': 12}
]

###############################################################################
# Question 1. Écriture et test de la fonction total_par_type                  #
###############################################################################

def total_par_type(mouvements, type_mouvement):
    pass # à remplacer par votre code


def test_total_par_type():
    pass # à remplacer par vos tests

###############################################################################
# Questions 2. et 3. Fonctions de calcul du solde                             #
###############################################################################

def solde_mensuel(mouvements, mois):
    """Calcule et renvoie le solde (recettes - dépenses) pour un mois donné."""
    total_recettes = 0
    total_depenses = 0

    for m in mouvements:
        if m['mois'] == mois:
            if m['type'] == 'recette':
                total_recettes += m['montant']
            else:
                total_depenses += m['montant']

    return total_recettes - total_depenses


def solde_annuel(mouvements):
    """Calcule et renvoie le solde annuel en additionnant les soldes de chaque
    mois."""
    total = 0
    # Parcourt les mois de l'année pour cumuler le bilan.
    for m in range(1, 13):
        total = total + solde_mensuel(mouvements, m)

    return total

# Question 2. Test de la fonction solde_anneul
def test_solde_annuel():
    pass # à remplacer par votre assertion


# Question 3. Calcul du solde du club (ajouter votre code ci-dessous)
 