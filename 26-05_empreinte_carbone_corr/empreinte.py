import os
import os.path
import json

###############################################################################
# Fonctions fournies                                                           
###############################################################################

def chargement_json(nom_fichier: str):
    """Charge le contenu d'un fichier JSON dans un dictionnaire Python
    renvoyé."""
    with open(nom_fichier, "r", encoding="utf8") as curseur:
        return json.load(curseur)


def sauvegarde_json(dictionnaire: dict, nom_fichier: str):
    """Sauvegarde le contenu d'un dictionnaire dans un fichier JSON."""
    with open(nom_fichier, "w", encoding="utf8") as curseur:
        json.dump(dictionnaire, curseur)


def est_dictionnaire(objet: any):
    """Teste si un objet est de type dictionnaire."""
    return isinstance(objet, dict)

###############################################################################
# Question 1. Fonction à implémenter après avoir consulté le contenu du fichier
# JSON agrégé `empreinte_ada_agr.json`.                                                   #
###############################################################################

def total_simple(empreinte: dict):
    """Fonction qui renvoie l'empreinte carbone totale d'un dictionnaire
    associant une empreinte carbone à des noms de catégories."""
    # On parcourt le dictionnaire et on accumule progressivement la somme des
    # valeurs de ce dictionnaire.
    somme = 0
    for cle in empreinte:
        somme += empreinte[cle]
    return somme


def test_total_simple():
    # Tests simples pour vérifier le bon fonctionnement de la fonction
    # (non demandés mais utiles).
    assert total_simple({}) == 0
    assert total_simple({"Logement": 2500, "Alimentation": 1500}) == 4000
    # Affichage de l'empreinte carbone totale de Ada
    ## Importation des données
    empreinte_ada_agr = chargement_json("empreinte_ada_agr.json")
    ## Calcul de l'empreinte carbone totale
    total_ada = total_simple(empreinte_ada_agr)
    ## Affichage du résultat
    print("Empreinte totale d'Ada :", total_ada, "kg de C02")
    

###############################################################################
# Question 2. Fonction à implémenter après avoir consulté le contenu du fichier
# JSON `empreinte_ada.json`. Remarque. L'approche récursive est nécessaire
# pour prendre en charge les sous-catégories.                      
###############################################################################

def total_rec(empreinte: dict):
    """Fonction récursive qui renvoie l'empreinte carbone totale représentée
    par un dictionnaire dont les valeurs peuvent aussi être des
    dictionnaires."""
    res = 0 # variable qui accumule les empreintes
    # Parcours en profondeur récursif classique d'un arbre d'arité non bornée
    # avec calcul de somme.
    for cle in empreinte:
        val = empreinte[cle]
        if not est_dictionnaire(val):
            # Cas de base : la valeur rencontrée est un entier
            res += val
        else:
            # Cas général : la valeur rencontrée est un dictionnaire. On
            # continue le parcours dans les sous-arbres.
            res += total_rec(val)
    return res


def test_total_rec():
    test_dico1 = {"a": 1, "d": 2}
    assert total_rec(test_dico1) == 3
    test_dico2 = {"a": {"b": 1, "c": 2}, "d": {"e": 3}}
    assert total_rec(test_dico2) == 6

###############################################################################
# Question 3. Fonction à analyser et corriger
###############################################################################

def alerte_valeur_aberrante(empreinte, limite):
    """Fonction censée déterminer si au moins une valeur du dictionnaire
    dépasse strictement la limite donnée."""
    for categorie, valeur in empreinte.items():
        if est_dictionnaire(valeur):
            # Si la valeur renvoyée ci-dessous est False (pas de détection
            # d'anomalie), la recherche s'interrompt avant d'avoir terminé le
            # parcours. C'est un cas classique de décrochage. Il faut donc
            # ne réaliser le renvoi qu'en cas de détection d'anomalie.
            return alerte_valeur_aberrante(valeur, limite)
        else:
            if valeur > limite:
                return True
    return False

def alerte_valeur_aberrante_corr(empreinte, limite):
    """Fonction censée déterminer si au moins une valeur du dictionnaire
    dépasse strictement la limite donnée."""
    for categorie, valeur in empreinte.items():
        if est_dictionnaire(valeur):
            # Si la valeur renvoyée ci-dessous est False (pas de détection
            # d'anomalie), la recherche s'interrompt avant d'avoir terminé le
            # parcours. C'est un cas classique de décrochage. Il faut donc
            # ne réaliser le renvoi qu'en cas de détection d'anomalie.
            if alerte_valeur_aberrante(valeur, limite):
                return True
        else:
            if valeur > limite:
                return True
    return False

def test_alerte_valeur_abrerrante_donnees_originales():
    # Ce test réussi alors que pour des raisons pédagogiques il ne devrait
    # échouer : la fonction est incorrecte mais les données originales ne
    # déclenchent pas d'erreur en raison de leur structure favorable.
    empreinte_ada_original = chargement_json("empreinte_ada_original.json")
    assert alerte_valeur_aberrante(empreinte_ada_original, 1000) == True

def test_alerte_valeur_abrerrante_donnees_modifiees():
    # Les données originales ont été modifiées en intervertissant simplement
    # "Alimentation" et "Logement". Cela est suffisant pour permettre le
    # déclenchement de l'erreur.
    empreinte_ada = chargement_json("empreinte_ada.json")
    assert alerte_valeur_aberrante(empreinte_ada, 1000) == True

###############################################################################
# Question 4. Jeu de tests pour la fonction alerte_valeur_aberrante
###############################################################################

def test_alerte_valeur_abrerrante_donnees_modifiees_corr():
    
    # Tests simples négatifs
    ## Dictionnaire vide
    assert not alerte_valeur_aberrante_corr({}, 1000)
    ## Dictionnaire simple sans anomalie
    assert not alerte_valeur_aberrante_corr({"a": 1, "d": 2}, 1000)
    ## Dictionnaire complexe sans anomalie
    test_dico1 = {"a": {"b": 1, "c": 2}, "d": {"e": 3}}
    assert not alerte_valeur_aberrante_corr(test_dico1, 1000)

    # Tests simples positifs
    ## Dictionnaire simple avec anomalie à gauche
    assert alerte_valeur_aberrante_corr({"a": 1500, "d": 2}, 1000)
    ## Dictionnaire simple avec anomalie à droite
    assert alerte_valeur_aberrante_corr({"a": 1, "d": 1500}, 1000)
    ## Dictionnaires imbriqués avec anomalie dans un sous dictionnaire à gauche
    test_dico2 = {"a": {"b": 1500, "c": 2}, "d": {"e": 3}}
    assert alerte_valeur_aberrante_corr(test_dico2, 1000)
    ## Dictionnaires imbriqués avec anomalie dans un sous dictionnaire à droite
    test_dico3 = {"a": {"b": 1, "c": 2}, "d": {"e": 1500}}
    assert alerte_valeur_aberrante_corr(test_dico3, 1000)

    # Test sur les données complètes
    empreinte_ada = chargement_json("empreinte_ada.json")
    assert alerte_valeur_aberrante_corr(empreinte_ada, 1000) == True


if __name__ == '__main__':
    # Pour l'affichage de la question 2.
    test_total_simple()