import ascii

###############################################################################
# Question 1. Écrire et tester la fonction bin2dec                            #
###############################################################################

def bin2dec(tuple_bin):
    dec = 0
    for i in range(len(tuple_bin)):
        bit = tuple_bin[i]
        puissance = len(tuple_bin) - i - 1
        dec += bit * 2 ** puissance
    return dec


def test_bin2dec():
    assert bin2dec((0, 1, 1, 0, 0, 0, 0, 1)) == 97
    assert bin2dec((0, 0, 1, 0, 1, 1, 1, 0)) == 46

###############################################################################
# Question 2. Écrire et tester la fonction qrcode2dec                         #
###############################################################################

def qrcode2dec(qrcode):
    res = []
    for tuple_bin in qrcode:
        res.append(bin2dec(tuple_bin))
    return res


def test_qrcode():
    assert qrcode2dec(ascii.qrcode_test1) == [78, 46, 83, 46, 73, 46]
    assert qrcode2dec(ascii.qrcode_test2) == [
        84, 101, 114, 109, 105, 110, 97, 108, 101
    ]

# Ajouter une instruction ci-desssous pour afficherla liste d'entiers
# décimaux correspondant au QR code de la figure 1.
print(qrcode2dec(ascii.qrcode_figure1))

# Écrire ci-contre à la place des ... la chaîne correspondante : "M.Hara"

###############################################################################
# Question 3. Tester puis corriger la fonction dec2str                        #                     
###############################################################################

def dec2str(liste_dec):
    """Prend en paramètre une liste d'entiers décimaux et renvoie la chaine de
    caractères formée des caractères correspondant de la table ASCII."""
    table_ascii = ascii.dict_ascii
    chaine = ""
    for entier in liste_dec:
        # branchement conditionnel ajouté ci-dessous pour ignore les valeurs
        # abhérentes (en effet sur un octet on peut coder les nombre entiers
        # de 0 à 255 aloers que les codes ascii dans l'exercice vont de 0 à
        # 127 (code ASCII dur 7 bits).
        if entier < 128:
            chaine += table_ascii[entier]
    return chaine


def test_dec2str():
    """Teste la fonction dec2str avec des données issues du module fourni"""
    print(dec2str(ascii.test1)) # passe 
    print(dec2str(ascii.test2)) # passe
    print(dec2str(ascii.test3)) # déclenche une erreur de clé car l'un des
    # nombres décimaux vaut 223 ce qui ne correspond à aucune clé du
    # dictionaire ASCII. Une solution est de simplement ignoré les valeurs
    # abhérentes.


# Décommenter la ligne ci-dessous à la question 3.
test_dec2str()

###############################################################################
# Question 4. Tester et corriger la fonction str2qrcode défectueuse           #
###############################################################################

def str2qrcode(message):
    """Convertit une chaine de caractères en liste de tuples binaires."""
    qrcode = []
    table_inverse = {valeur: cle for cle, valeur in ascii.dict_ascii.items()}

    for caractere in message:
        decimal = table_inverse[caractere]
        liste_bits = []
        while decimal > 0:
            liste_bits = [decimal % 2] + liste_bits
            decimal = decimal // 2
        # Ligne ajoutée ci-dessous pour que toutes les lignes possèdent 8
        # cases. Il faut parfois ajouter des cases de zéros manquants par la
        # gauche.
        liste_bits = (8 - len(liste_bits)) * [0] + liste_bits
        ligne = tuple(liste_bits) # conversion de la liste liste_bits en tuple
        qrcode.append(ligne)
    return qrcode


def test_str2qrcode():
    # test avec un qrcode fourni dans le module ascii.py
    assert str2qrcode("N.S.I.") == ascii.qrcode_test

# Écrire ci-dessous une ou plusieurs instructions pour afficher le qrcode
# produit par la fonction str2qrcode avec la chaîne trouvée à la question 2.
qrcode = str2qrcode("M.Hara")
for ligne in qrcode:
    print(ligne)