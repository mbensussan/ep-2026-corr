import ascii

###############################################################################
# Question 1. Écrire et tester la fonction bin2dec                            #
###############################################################################

def bin2dec(tuple_bin):
    pass # à remplacer par votre code


def test_bin2dec():
    pass # à remplacer par deux assertions

###############################################################################
# Question 2. Écrire et tester la fonction qrcode2dec                         #
###############################################################################

def qrcode2dec(qrcode):
    pass # à remplacer par votre code


def test_qrcode():
    assert qrcode2dec(ascii.qrcode_test1) == [78, 46, 83, 46, 73, 46]
    assert qrcode2dec(ascii.qrcode_test2) == [
        84, 101, 114, 109, 105, 110, 97, 108, 101
    ]

# Ajouter une instruction ci-desssous pour afficherla liste d'entiers
# décimaux correspondant au QR code de la figure 1.


# Écrire ci-contre à la place des ... la chaîne correspondante : "..."

###############################################################################
# Question 3. Tester puis corriger la fonction dec2str                        #                     
###############################################################################

def dec2str(liste_dec):
    """Prend en paramètre une liste d'entiers décimaux et renvoie la chaine de
    caractère formée des caractères correspondant de la table ASCII."""
    table_ascii = ascii.dict_ascii
    chaine = ""
    for entier in liste_dec:
        chaine += table_ascii[entier]
    return chaine


def test_dec2str():
    """Teste la fonction dec2str avec des données issues du module fourni"""
    print(dec2str(ascii.test1))
    print(dec2str(ascii.test2))
    print(dec2str(ascii.test3))


# Décommenter la ligne ci-dessous à la question 3.
# test_dec2str()

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
        ligne = tuple(liste_bits) # conversion de la liste liste_bits en tuple
        qrcode.append(ligne)
    return qrcode


def test_str2qrcode():
    # test avec un qrcode fourni dans le module ascii.py
    assert str2qrcode("N.S.I.") == ascii.qrcode_test

# Écrire ci-dessous une ou plusieurs instructions pour afficher le qrcode
# produit par la fonction str2qrcode avec la chaîne trouvée à la question 2.
