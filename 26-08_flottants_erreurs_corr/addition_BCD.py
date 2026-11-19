###############################################################################
# Question 1 : Mise en évidence du problème des flottants                     #
###############################################################################
# Écrire ci-dessous la fonction calcul_recettes() et son appel

def calcul_recettes():
    nb_restos = 1000
    nb_menus_vendus_pas_jour_par_resto = 500
    nb_menus_vendus_par_jour = nb_menus_vendus_pas_jour_par_resto * nb_restos
    prix_menu = 2.27 + 5.19 + 1.81
    res = 0
    for _ in range(nb_menus_vendus_par_jour):
        res += prix_menu
    return res

print(2.27 + 5.19 + 1.81)
print(calcul_recettes())

# question 1. pour exliquer le problème il suffit de citer l'énoncé. On peut
# également afficher le résultat de 2.27 + 5.19 + 1.81  qui est évalué à
# 9.270000000000001 (au lieu de l'attendu 9.27).

###############################################################################
# Question 2 : Conversion BCD vers Décimal                                    #
###############################################################################

def convertir_BCD_vers_decimal(liste_quartets):
    """Prend en paramètre une liste de chaînes de caractères représentant des
    quartets BCD, et renvoie la valeur décimale correspondante dans une chaîne
    de caractères."""
    resultat_dec_str = ''
    # On parcourt la liste des quartets. 
    for i in range(len(liste_quartets)):
        # On convertit chaque quartet enchiffre décimal (int).
        chiffre_dec_int = 0
        puissance = 3
        for bit in liste_quartets[i]:
            chiffre_dec_int += int(bit) * 2 ** puissance
            puissance -= 1
        # Si on se trouve à l'avant dernier quartet, on place le séparateur
        # décimal ('.') avant d'ajouter le chiffre décimal.
        if i == len(liste_quartets) - 2:
            resultat_dec_str += '.'
        # On convertit en chaîne de caractère le chiffre décimal obtenu pour
        # l'ajouter à la chaîne résultat.
        resultat_dec_str += str(chiffre_dec_int)
    # En fin de parcoours, on convertit la chaîne obtenue en flottant.
    return resultat_dec_str


def test_convertir_BCD_vers_decimal():
    assert convertir_BCD_vers_decimal(['0001', '0011', '0101', '0110']) == '13.56'
    assert convertir_BCD_vers_decimal(['0101', '1001', '0000', '0000']) == '59.00'
    assert convertir_BCD_vers_decimal(['0001', '0111', '0101']) == '1.75'
    assert convertir_BCD_vers_decimal(['0000', '0010', '0011']) == '0.23'

###############################################################################
# Code fourni pour les questions 3 et 4                                       #
###############################################################################

def convertir_dec_vers_BCD(decimal):
    """Convertit une chaîne représentant un décimal vers une liste de quartets
    BCD. Convention : virgule implicite avant les deux derniers quartets."""
    ajouter_zero = False
    liste_quartets = []

    if '.' not in decimal:
        decimal = decimal + '.00'

    for i in range(len(decimal)):
        if decimal[i] != '.':
            quartet = bin(int(decimal[i]))[2:].zfill(4)
            liste_quartets.append(quartet)

        # Si le nombre n'a qu'un seul chiffre après la virgule
        if decimal[i] == '.' and i == len(decimal) - 2:
            ajouter_zero = True

    if ajouter_zero:
        liste_quartets.append('0000')

    return liste_quartets


def additionner_binaire_quartets(quartet1, quartet2, retenue):
    """Additionne bit à bit deux quartets binaire purs. Renvoie un tuple
    (somme_binaire_str, nouvelle_retenue_int)."""
    somme = ""
    for i in range(4):
        # Lecture de la droite vers la gauche
        bit1 = int(quartet1[3 - i])
        bit2 = int(quartet2[3 - i])
        total = bit1 + bit2 + retenue

        if total == 0:
            somme = '0' + somme
            retenue = 0
        elif total == 1:
            somme = '1' + somme
            retenue = 0
        elif total == 2:
            somme = '0' + somme
            retenue = 1
        elif total == 3:
            somme = '1' + somme
            retenue = 1

    return somme, retenue


def corriger_BCD(somme, retenue):
    """Applique la correction BCD si le quartet dépasse 9 ou génère une
    retenue. Ajoute '0110' (6) au quartet invalide."""
    # Si somme >= 10 ('1010' ou '1011' ou '1100' etc.)
    if somme[0] == '1' and (somme[1] == '1' or somme[2] == '1'):
        somme, retenue = additionner_binaire_quartets(somme, '0110', 0)
        return somme, retenue

    # S'il y a eu dépassement naturel lors de l'addition binaire
    if retenue == 1:
        somme, _ = additionner_binaire_quartets(somme, '0110', 0)
        return somme, retenue
        
    return somme, retenue


def aligner_quartets(q1, q2):
    """Doit équilibrer les deux listes de quartets passée en paramètre en
    ajoutant des '0000' à gauche de la liste la plus courte. Renvoie ensuite
    les deux listes après modification dans un tuple"""
    nb_quartets_ajout = abs(len(q1) - len(q2))
    if len(q1) < len(q2):
        q1 = nb_quartets_ajout * ['0000'] + q1
    else:
        q2 = nb_quartets_ajout * ['0000'] + q2
    return q1, q2


def additionner_nombres_format_BCD(a, b):
    """Additionne deux nombres au format BCD, quartet par quartet."""
    liste_quartets1 = convertir_dec_vers_BCD(a)
    liste_quartets2 = convertir_dec_vers_BCD(b)

    # Ajustement de la longueur
    liste_quartets1, liste_quartets2 = aligner_quartets(liste_quartets1, liste_quartets2)

    retenue = 0
    resultat = []
    longueur_max = max(len(liste_quartets1), len(liste_quartets2)) 

    for i in range(longueur_max):
        indice = longueur_max - i - 1
        
        # Addition binaire simple des quartets
        somme, retenue = additionner_binaire_quartets(liste_quartets1[indice], liste_quartets2[indice], retenue)
        # Question 3. correction ajoutée ci-dessous
        somme, retenue = corriger_BCD(somme, retenue) # correction
        resultat = [somme] + resultat

    # Gestion de la dernière retenue éventuelle
    if retenue == 1:
        resultat = ['0001'] + resultat
        
    return resultat


def test_additionner_nombres_format_BCD():
    # à compléter à la question 3.
    assert additionner_nombres_format_BCD('27', '35') == convertir_dec_vers_BCD('62')
    # à compléter à la question 4.
    assert additionner_nombres_format_BCD('23', '4') == convertir_dec_vers_BCD('27')