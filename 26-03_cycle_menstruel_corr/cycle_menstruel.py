import calendar
import pytest # ajouté pour vérifier la levé d'une erreur d'assertion

###############################################################################
# Écrire le code de la fonction est_bissextile de la question 1               #
###############################################################################

def est_bissextile(annee):
    """Prend en paramètre un entier correspondant à une année et renvoie un
    booléen indiquant si cette année est bissextile."""
    return annee % 4 == 0 and (not annee % 100 == 0 or annee % 400 == 0)


def test_est_bissextile():
    assert est_bissextile(2024) == True
    assert est_bissextile(2100) == False
    assert est_bissextile(2000) == True

###############################################################################
# Écrire le code de la fonction determiner_phase de la question 2             #
###############################################################################

def determiner_phase(jour):
    """Prend en paramètre un entier(compris entre 1 et 28 inclus) qui
    correspond au jour d’un cycle et qui renvoie un entie correspondant au
    numéro de la phase associée."""
    assert jour in range(1, 29), "jour doit être un entier entre 1 et 28 !"
    if jour < 6:
        return 1
    elif jour < 14:
        return 2
    elif jour == 14:
        return 3
    else:
        return 4
    

def test_determiner_phase():
    with pytest.raises(AssertionError):
        determiner_phase(0) # appel incorrect : argument hors plage 1 - 28
        determiner_phase(29) # appel incorrect : argument hors plage 1 - 28
        determiner_phase(2.5) # appel incorrect : argument flottant
    assert determiner_phase(3) == 1
    assert determiner_phase(8) == 2
    assert determiner_phase(14) == 3
    assert determiner_phase(20) == 4

###############################################################################
# Fonctions fournies pour la question 3                                       #
###############################################################################

def jours_dans_mois(annee, mois):
    """Renvoie le nombre de jours dans un mois donné d'une année donnée.
    Utilise le module calendar pour gérer les années bissextiles."""
    if mois == 2:  # février
        return 29 if calendar.isleap(annee) else 28
    elif mois in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30


def ajouter_jours(date, nb_jours):
    """Ajoute nb_jours à une date donnée et renvoie la nouvelle date.
    La date est représentée par un tuple (jour, mois, année)."""
    jour, mois, annee = date
    jour = jour + nb_jours

    # Ajustement du jour et du mois si dépassement
    while jour > jours_dans_mois(annee, mois):
        jour = jour - jours_dans_mois(annee, mois)
        mois = mois + 1
        if mois > 12:  # passage à l'année suivante
            mois = 1
            annee = annee + 1

    return (jour, mois, annee)


def test_ajouter_jours():
    # Sans changement de mois ou d'année
    assert ajouter_jours((7, 9, 2025), 3) == (10, 9, 2025)
    # Avec changement de mois (hors mois de février)
    assert ajouter_jours((28, 9, 2025), 5) == (3, 10, 2025)
    # Avec changement de mois (mois de février, année non-bissextile)
    assert ajouter_jours((27, 2, 2025), 5) == (4, 3, 2025)
    # Avec changement de mois (mois de février, année bissextile)
    assert ajouter_jours((27, 2, 2024), 5) == (3, 3, 2024)
    # Avec changement de mois et d'année
    assert ajouter_jours((25, 12, 2025), 8) == (2, 1, 2026)
    
    
###############################################################################
# Fonction fournie pour la question 4                                         #
###############################################################################

def calendrier_cycles(date_regles):
    """Renvoie une chaîne de caractère contenant au format iCalendar,
    l'ensemble des dates de début de règles qui se présentent dans les 100
    jours suivants `date_regles`, date incluse.

    Hypothèse : cycle régulier de 28 jours."""

    cal_lignes = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:']

    date_courante = date_regles
    jours_ecoules = 0

    # On ajoute les dates tant que l'on ne dépasse pas 100 jours écoulés
    while jours_ecoules + 28 <= 100:
        jour, mois, annee = date_courante  
        cal_lignes.append('BEGIN:VEVENT')
        cal_lignes.append('SUMMARY: Règles')
        # Problème : les date ajoutées à la chaîne de caractère ne vérifie pas
        # le format aaaammjj car certains jours ou mois sont à un seul chiffre.
        # Il faut donc ajouter un zéro lorsque cela est nécessaire.
        date = str(annee) + str(mois) + str(jour)
        cal_lignes.append('DTSTART:' + date)
        cal_lignes.append('END:VEVENT')
        date_courante = ajouter_jours(date_courante, 28)
        jours_ecoules += 28 

    cal_lignes.append('END:VCALENDAR')

    # La méthode join va renvoyer ici une unique chaîne contenant toutes les
    # chaînes de la liste séparées par des sauts de lignes.
    return '\n'.join(cal_lignes)


def calendrier_cycles_v2(date_regles):
    """Renvoie une chaîne de caractère contenant au format iCalendar,
    l'ensemble des dates de début de règles qui se présentent dans les 100
    jours suivants `date_regles`, date incluse.

    Hypothèse : cycle régulier de 28 jours."""

    cal_lignes = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:']

    date_courante = date_regles
    jours_ecoules = 0

    # On ajoute les dates tant que l'on ne dépasse pas 100 jours écoulés
    while jours_ecoules + 28 <= 100:
        jour, mois, annee = date_courante  
        cal_lignes.append('BEGIN:VEVENT')
        cal_lignes.append('SUMMARY: Règles')
        # Problème : les date ajoutées à la chaîne de caractère ne vérifie pas
        # le format aaaammjj car certains jours ou mois sont à un seul chiffre.
        # Il faut donc ajouter un zéro lorsque cela est nécessaire.
        annee_str = str(annee)
        mois_str = str(mois)
        jour_str = str(jour)
        if len(mois_str) == 1:
            mois_str = '0' + mois_str
        if len(jour_str) == 1:
            jour_str = '0' + jour_str
        date = annee_str + mois_str + jour_str
        cal_lignes.append('DTSTART:' + date)
        cal_lignes.append('END:VEVENT')
        date_courante = ajouter_jours(date_courante, 28)
        jours_ecoules += 28 

    cal_lignes.append('END:VCALENDAR')

    # La méthode join va renvoyer ici une unique chaîne contenant toutes les
    # chaînes de la liste séparées par des sauts de lignes.
    return '\n'.join(cal_lignes)


def test_calendrier_cycles():
    """Crée un calendrier et le charge avec le module ics pour vérifier sa
    validité. Nécessite que le module ics soit présent sur la machine
    (pip install ics)."""
    from ics import Calendar
    c = calendrier_cycles((12, 3, 2026))
    print(c)
    cal = Calendar(c)
    print(cal.events)


def test_calendrier_cycles_v2():
    """Crée un calendrier et le charge avec le module ics pour vérifier sa
    validité. Nécessite que le module ics soit présent sur la machine
    (pip install ics)."""
    from ics import Calendar
    c = calendrier_cycles_v2((12, 3, 2026))
    print(c)
    cal = Calendar(c)
    print(cal.events)


if __name__ == '__main__':
    print("\nAvant correction : dates au mauvais format\n")
    c = calendrier_cycles((12, 3, 2026))
    print(c)
    print("\nAprès correction : dates au bon format\n")
    c2 = calendrier_cycles_v2((12, 3, 2026))
    print(c2)