import donnees
import donnees_completes
from math import sqrt


def salaire_moyen_condition(employes, champ, valeur):
    """Renvoie le salaire moyen des employes ayant val comme valeur associée
    au champ donné en argument. Si le nombre d'employés considéré est nul,
    cette fonction renvoie None."""
    nbre_employes_filtres = 0
    somme_salaires = 0
    # On parcourt la liste d'employés en comptant les employés correspondant au
    # filtre choisi et en accumulant leurs salaires.
    for e in employes:
        if e[champ] == valeur:
            somme_salaires += e['salaire']
            nbre_employes_filtres += 1
    # Si le filtre n'a retenu aucun employé, on renvoie None. Sinon, on renvoie
    # la moyenne des salaires des employés retenus.
    if nbre_employes_filtres == 0:
        return None
    else:
        return somme_salaires / nbre_employes_filtres


def test_salaire_moyen_condition():
    e = donnees.employes
    assert salaire_moyen_condition([], 'sexe', 'F') == None
    assert salaire_moyen_condition(e, 'sexe', 'F') == 2400.0
    assert salaire_moyen_condition(e, 'etudes', 3) == 2550.0
    assert salaire_moyen_condition(e, 'etudes', 12) == None


def effectif_par_sexe(employes):
    """Renvoie un dictionnaire ayant deux clés 'F' et 'M' associée
    respectivement au nombre d'employées femmes et au nombre d'employés hommes
    dans les données en arguments."""
    res = {'F': 0, 'M': 0}
    for e in employes:
        res[e['sexe']] += 1
    return res


def test_effectif_par_sexe():
    e = donnees.employes
    assert effectif_par_sexe(e) == { 'F' : 3, 'M' : 3 }


def calcul_ecart_sexe(employes):
    """Renvoie l'écart de salaire en pourcentage pour les femmes par rapport
    aux hommes."""
    moy_h = salaire_moyen_condition(employes, 'sexe', 'M')
    # erreur 1: le premier argument 'employes' (type str) devrait être le
    # paramètre employes sans guillemets qui correspond à une liste de
    # dictionnaires dans laquelle chaque dictionnaire représente un employé.
    moy_f = salaire_moyen_condition('employes', 'sexe', 'F')
    # erreur 2 : cas de l'absence d'un sexe oublié
    # erreur 3 : formule incorrecte/incomplète
    return moy_h - moy_f


def calcul_ecart_sexe_v2(employes):
    """Renvoie l'écart de salaire en pourcentage pour les femmes par rapport
    aux hommes."""
    moy_h = salaire_moyen_condition(employes, 'sexe', 'M')
    # erreur 1: le premier argument 'employes' (type str) devrait être le
    # paramètre employes sans guillemets qui correspond à une liste de
    # dictionnaires dans laquelle chaque dictionnaire représente un employé.
    # ligne incorrecte :
    # moy_f = salaire_moyen_condition('employes', 'sexe', 'F')
    # ligne correcte :
    moy_f = salaire_moyen_condition(employes, 'sexe', 'F')
    # erreur 2 : cas de l'absence d'un sexe oublié
    effectifs = effectif_par_sexe(employes)
    if effectifs['F'] == 0 or effectifs['M'] == 0:
        return None
    else:
        # erreur 3 : formule incorrecte/incomplète
        # ligne incorrecte :
        #return moy_h - moy_f
        # ligne correcte :
        return (moy_h - moy_f) / moy_h * 100
    
def test_calcul_ecart_sexe():
    femmes = [e for e in donnees.employes if e['sexe'] == 'F']
    hommes = [e for e in donnees.employes if e['sexe'] == 'M']
    assert calcul_ecart_sexe(femmes) == None
    assert calcul_ecart_sexe(hommes) == None
    ecart = calcul_ecart_sexe(donnees.employes)
    assert ecart >= 0 and ecart <= 100

def test_calcul_ecart_sexe_v2():
    femmes = [e for e in donnees.employes if e['sexe'] == 'F']
    hommes = [e for e in donnees.employes if e['sexe'] == 'M']
    assert calcul_ecart_sexe_v2(femmes) == None
    assert calcul_ecart_sexe_v2(hommes) == None
    ecart = calcul_ecart_sexe_v2(donnees.employes)
    assert ecart >= 0 and ecart <= 100



# Attribution d'un premier salaire après embauche par les k plus proches
# voisins


def sexe_vers_entier(e):
    if e['sexe'] == 'F':
        return 1
    else:
        return -1


def distance(e1, e2):
    """Renvoie la mesure de distance entre deux personnes."""
    s = 0
    # ligne à supprimer : il ne faut pas tenir compte du sexe pour le calcul
    # de la distance.
    s = s + (sexe_vers_entier(e1) - sexe_vers_entier(e2))**2
    s = s + (e1['experience'] - e2['experience'])**2
    s = s + (e1['etudes'] - e2['etudes'])**2
    return sqrt(s)

def distance_v2(e1, e2):
    """Renvoie la mesure de distance entre deux personnes."""
    s = 0
    # ligne à supprimée : il ne faut pas tenir compte du sexe pour le calcul
    # de la distance.
    #s = s + (sexe_vers_entier(e1) - sexe_vers_entier(e2))**2
    s = s + (e1['experience'] - e2['experience'])**2
    s = s + (e1['etudes'] - e2['etudes'])**2
    return sqrt(s)


def k_plus_proches(k, employes, e):
    """Renvoie les k employes les plus proches de e par la 
    distance définie au dessus."""
    e_d = [(distance(e, employes[i]), i) for i in range(len(employes))]
    e_d.sort() # va trier en premier sur la distance
    voisins = []
    for i in range(k):
        voisins.append(employes[e_d[i][1]])
    return voisins

def k_plus_proches_v2(k, employes, e):
    """Renvoie les k employes les plus proches de e par la 
    distance définie au dessus."""
    e_d = [(distance_v2(e, employes[i]), i) for i in range(len(employes))]
    e_d.sort() # va trier en premier sur la distance
    voisins = []
    for i in range(k):
        voisins.append(employes[e_d[i][1]])
    return voisins


def salaire_moyen(employes):
    """Renvoie le salaire moyen pour une liste d'employes"""
    if len(employes) == 0:
        return None
    s = sum(e['salaire'] for e in employes)
    return s/len(employes)


def salaire_par_proximite(employes, e):
    """Prend en entrée une liste d'employés et un dictionnaire comportant
    les champs experience, etudes et sexe et renvoie le salaire le plus
    proche en moyennant les 3 plus proches voisins."""
    voisins = k_plus_proches(3, employes, e)
    return salaire_moyen(voisins)

def salaire_par_proximite_v2(employes, e):
    """Prend en entrée une liste d'employés et un dictionnaire comportant
    les champs experience, etudes et sexe et renvoie le salaire le plus
    proche en moyennant les 3 plus proches voisins."""
    voisins = k_plus_proches_v2(3, employes, e)
    return salaire_moyen(voisins)


if __name__ == '__main__':
    emps = donnees_completes.employes
    sal_moy_fem = salaire_moyen_condition(emps, 'sexe', 'F')
    sal_moy_hom = salaire_moyen_condition(emps, 'sexe', 'M')
    print("Données complètes :")
    print('Salaire moyen des femmes :', round(sal_moy_fem, 2), 'Euros')
    print('Salaire moyen des hommes :', round(sal_moy_hom, 2), 'Euros')
    femme1 = {'experience': 3, 'etudes': 3, 'sexe': 'F'}
    homme1 = {'experience': 3, 'etudes': 3, 'sexe': 'M'}
    sal_fem = salaire_par_proximite(emps, femme1)
    sal_hom = salaire_par_proximite(emps, homme1)
    sal_fem2 = salaire_par_proximite_v2(emps, femme1)
    sal_hom2 = salaire_par_proximite_v2(emps, homme1)
    print("Salaire proposés pour une femme et un homme ayant les mêmes niveau")
    print("d'étude et nombre d'années d'expérience :")
    print("Avant correction :")
    print("Femme : ", round(sal_fem, 2), "Euros")
    print("Homme: ", round(sal_hom, 2), "Euros")
    print("Après correction :")
    print("Femme : ", round(sal_fem2, 2), "Euros")
    print("Homme: ", round(sal_hom2, 2), "Euros")