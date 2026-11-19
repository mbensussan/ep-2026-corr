from PIL import Image

###############################################################################
# Réponse à la question 1.
# Il suffit d'exhiber un contre exemple. Par codage RLE la liste [0] donne
# [1, 0] (une fois le nombre zéro). On voit ainsi clairement que le codage RLE
# peut être plus long que la liste de départ.
###############################################################################


def codage_rle(liste_octets):
    """Renvoie une liste d'octets obtenue par compression RLE."""
    # On part d'une liste résultat vide.
    liste_rle = []
    i = 0
    # On parcourt la liste d'octets
    while i < len(liste_octets):
        # c représente le premier octet de la zone d'octets identiques courante
        c = liste_octets[i]
        # On commence le décompte à 1.
        k = 1
        # Tant que l'on a pas atteint la fin de la liste d'octet et la fin de
        # la zone d'octets identiques
        while i+k < len(liste_octets) and liste_octets[i+k] == c:
            # on incrémente la variable compteur.
            k += 1
        # En fin de zone d'octets identiques, on ajoute le nombre de
        # répétitions et la valeur de l'octet dans la liste résultat.
        liste_rle.append(k)
        liste_rle.append(c)
        # On saute ensuite au début de la zone d'octets identiques suivante.
        i += k
    return liste_rle


def decodage_rle(liste_rle):
    """Renvoie la liste d'octets obtenue à partir de la liste liste_rle obtenue
    par compression RLE."""
    # On part d'un liste résultat vide.
    liste_octets = []
    # On parcourt la liste obtenue par codage RLE avec un pas de deux. On prend
    # soin de choisir comme borne supérieure len(liste_rle) - 1 pour éviter le
    # dépassement d'indice.
    for i in range(0, len(liste_rle) - 1, 2):
        # À chaque itération,
        # l'élément i correspond au nombre de répétitions,
        repets = liste_rle[i]
        # l'élément i + 1 correspond à l'octet répété,
        octet = liste_rle[i+1]
        # on ajoute dans la liste résultat le bon nombre de cases contenant
        # l'octet répété.
        liste_octets += repets * [octet]
    return liste_octets


def test_codage():
    assert codage_rle([255, 255, 0, 255, 255, 255]) == [2, 255, 1, 0, 3, 255]
    assert decodage_rle([2, 255, 1, 0, 3, 255]) == [255, 255, 0, 255, 255, 255]


# Code ajouté pour répondre à la question 4.
# Il suffisait de modifier légèrement la fonction codage_rle sans modifier la
# fonction decodage_rle

def codage_rle_v2(liste_octets):
    """Renvoie une liste d'octets obtenue par compression RLE."""
    # On part d'une liste résultat vide.
    liste_rle = []
    i = 0
    # On parcourt la liste d'octets
    while i < len(liste_octets):
        # c représente le premier octet de la zone d'octets identiques courante
        c = liste_octets[i]
        # On commence le décompte à 1.
        k = 1
        # Tant que l'on a pas atteint la fin de la liste d'octet et la fin de
        # la zone d'octets identiques et que la longeur de cette zone ne
        # dépasse pas 255 (pour éviter la saturation lors de l'utilisation de
        # la fonction enregistrer_octet). On a juste ajouté ` and k < 255`.
        while i+k < len(liste_octets) and liste_octets[i+k] == c and k < 255:
            # on incrémente la variable compteur.
            k += 1
        # En fin de zone d'octets identiques, on ajoute le nombre de
        # répétitions et la valeur de l'octet dans la liste résultat.
        liste_rle.append(k)
        liste_rle.append(c)
        # On saute ensuite au début de la zone d'octets identiques suivante.
        i += k
    return liste_rle


def test_codage_v2():
    # Tests permettant de vérifier le comportement en cas de répététions
    # supérieure à 255 (saturation).
    assert codage_rle_v2(258 * [100]) == [255, 100, 3, 100]
    assert decodage_rle([255, 100, 3, 100]) == 258 * [100]


def enregistrer_octets(nom_fichier, liste_octets):
    """Enregistre une liste de valeurs numériques entre 0 et 255 dans le
    fichier nom_fichier. Si une valeur est plus grande que 255 on considère
    que c'est 255. De même pour les valeur plus petite que 0."""
    # Le fichier est ouvert en mode binaire pour pouvoir écrire sans
    # restriction toute valeur entre 0 et 255.
    with open(nom_fichier, 'wb') as fichier:
        # Pour convertir une liste de valeur entre 0 et 255 en une liste
        # d'octets qui peuvent être écrits dans le fichier, on utilise `bytes`.
        fichier.write(bytes([max(0, min(255, b)) for b in liste_octets]))


def charger_octets(nom_fichier):
    """Renvoie la liste des octets présents dans le fichier nom_fichier."""
    with open(nom_fichier, 'rb') as fichier:
        liste_octets = list(fichier.read())
        return liste_octets


def enregistrer_image(nom_image, largeur, liste_niveaux):
    """Enregistre un fichier image nom_image de la largeur donnée et dont les 
    valeurs de niveaux de gris des pixels sont celles de la liste
    liste_niveaux."""
    hauteur = len(liste_niveaux) // largeur
    im = Image.frombytes('L', (largeur, hauteur), bytes(liste_niveaux))
    im.save(nom_image)


def charger_image(nom_image):
    """Étant donné une image nom_image, renvoie un couple
    (largeur, liste_niveaux) où largeur est la largeur de l'image et
    liste_niveaux est la liste des valeurs de niveaux de gris de l'image ligne
    par ligne."""

    image = Image.open(nom_image).convert('L')
    return (image.width, list(image.tobytes()))

###############################################################################
# Fonction nécessaire pour les tests de la question 3                         #
###############################################################################


def encoder_decoder_image(nom_image):
    """Fonction de test permettant d'encoder puis décoder une image avec un
    codage RLE. Le fichier rle est nommé nom_image.rle et le fichier decodé
    est nom_image.dec.png ."""
    w, l = charger_image(nom_image)
    enregistrer_octets(nom_image+'.rle', codage_rle(l))
    l = charger_octets(nom_image+'.rle')
    enregistrer_image(nom_image+'.dec.png', w, decodage_rle(l))

# Code ajouté pour répondre à la question 4.

def encoder_decoder_image_v2(nom_image):
    """Fonction de test permettant d'encoder puis décoder une image avec un
    codage RLE. Le fichier rle est nommé nom_image.rle et le fichier decodé
    est nom_image.dec.png ."""
    w, l = charger_image(nom_image)
    enregistrer_octets(nom_image+'.rle', codage_rle_v2(l))
    l = charger_octets(nom_image+'.rle')
    enregistrer_image(nom_image+'.dec.v2.png', w, decodage_rle(l))


# Code ajouté
# Pour rappel, if if __name__ == '__main__': permet que le code contenu dans
# ce branchement conditionnel ne soit exécuté que si l'exécution est lancé
# depuis ce programme. Autrement dit ce programme est le programme principal.
if __name__ == '__main__':
    # Pour la question 3.
    encoder_decoder_image('bac_nsi_32.png')
    encoder_decoder_image('bac_nsi_256.png')
    # Résultat obtenu :
    # On voit que sur l'image de petite taille, les étapes de codage puis de
    # décodage ont conservé l'image intacte. Ce n'est pas le cas de l'image de
    # grande taille qui a été altéré avec l'apparition de décallages.
    # Pour la question 4.
    encoder_decoder_image_v2('bac_nsi_32.png')
    encoder_decoder_image_v2('bac_nsi_256.png')
    # Les images produites à l'aide de la fonction codage_rle_v2 sont
    # maintenant intactes après décodage.