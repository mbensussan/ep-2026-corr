import csv

class Renard:

    """Classe représentant un renard dans le refuge.
    Attributs : identifiant, nom, poids, date_arrivee."""

    def __init__(self, identifiant, nom, poids, date_arrivee):
        self.identifiant = identifiant
        self.nom = nom
        self.poids = poids
        self.date_arrivee = date_arrivee

    def __str__(self):
        return f"Renard ID {self.identifiant} - {self.nom} (Arrivé le {self.date_arrivee})"


class Refuge:

    """Classe représentant le refuge contenant la liste des renards."""

    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse
        self.liste_renards = []
        
    def recueillir(self, un_renard):
        """Méthode d'ajout d'un renard au refuge."""
        self.liste_renards.append(un_renard)

    def lister_peu_corpulents(self):
        """Méthode qui renvoie une liste des Renards dont le poids est
        inférieur srictement à 6.0 kg."""
        return [renard for renard in self.liste_renards if renard.poids < 6.0]

    def pourcentage_peu_corpulents(self):
        """Méthode qui renvoie le pourcentage des renards peu corpulents."""
        if len(self.liste_renards) == 0:
            return 0.0
        return len(self.lister_peu_corpulents()) / len(self.liste_renards) * 100

    def importer_donnees(self, nom_fichier):
        """Méthode qui importe les données des renards à partir d'un fichier
        CSV."""
        print(f"Tentative d'importation depuis {nom_fichier}...")
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            lignes = csv.DictReader(f, delimiter=';')
            for ligne in lignes:
                # question 3. Tout est importé en chaîne de caractères. Il
                # fallait convertir en nombre les données pertinentes
                # (ligne['id'] en entier et ligne['poids'] en flottant)
                renard = Renard(int(ligne['id']), ligne['nom'], float(ligne['poids']), ligne['date_arrivee'])
                self.recueillir(renard)


if __name__ == '__main__':
    renard1 = Renard(200, 'Oscar', 5.1, '2026-01-01')
    print(renard1)
    refuge1 = Refuge("SOS Goupil", "10, Av. du Général de Gaulle, 94700 Maison-Alfort")
    refuge1.importer_donnees("./26-12_refuge_renards_corr/donnees_renards.csv")
    print(refuge1.pourcentage_peu_corpulents())
    nbre_renards_peu_corpulents = len(refuge1.lister_peu_corpulents())
    nbre_renards_total = len(refuge1.liste_renards)
    print("Nombre de renards peu corpulents :", nbre_renards_peu_corpulents)
    print("Nombre de renards hébergés :", nbre_renards_total)
    pourcentage = nbre_renards_peu_corpulents / nbre_renards_total * 100
    print("Pourcentagede peu corpulents :", round(pourcentage))