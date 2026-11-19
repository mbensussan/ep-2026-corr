import random

class Coccinelle:
    
    def __init__(self, sexe: str, age: int, niv_nutrition: int):
        self.age = age
        self.esperance_de_vie = random.randint(200, 350)
        self.sexe = sexe
        self.niv_nutrition = niv_nutrition

    def chasser(self, nb_proies, nb_coccinelles):
        """Méthode à la fois accesseur et mutateur.
        Renvoie :
            le nombre de pucerons restants après la chasse de la coccinelle.
            Le nombre de pucerons mangés par la coccinelle est généré
            aléatoirement mais dépend du nombre pucerons disponibles
            (`nb_proies`) et du nombre de coccinelles en concurrence
            (`nb_coccinelles`).
        Modifie :
            le niveau de nutrition de la coccinelle (attribut `niv_nutrition`)
            qui augmente si la coccinelle a mangé suffisamment de de pucerons
            (10) ou diminue dans le cas contraire ce qui mène éventuellement à
            sa mort si ce niveau atteint 0.
        """
        # coccinelle morte
        if nb_coccinelles == 0:
            # on renvoie le nombre de pucerons inchangé.
            return nb_proies
        # sinon on calcule le nombre de pucerons moyen par coccinelle
        proies_par_cocci = nb_proies / nb_coccinelles

        # en fonction de ce nombre, la coccinelle peu plus ou moins se nourrir
        if proies_par_cocci > 20:
            consomme = random.randint(12, 20)
        elif proies_par_cocci > 10:
            consomme = random.randint(8, 15)
        else:
            consomme = random.randint(3, 8)
        # cette ligne sert à ne pas dépasser le nombre de pucerons disponibles
        consomme = min(consomme, nb_proies)
        # bilan : modification du niveau de nutrition de la coccinelle
        if consomme >= 10:
            self.niv_nutrition += 1
        else:
            self.niv_nutrition = max(0, self.niv_nutrition - 1)
        # calcul et renvoie du nombre de pucerons restants
        return nb_proies - consomme

    def reproduction(self):
        """Une femelle avec un niveau de nutrition >= 2 engendre exactement
        deux descendants : un mâle et une femelle."""
        descendants = []
        # Question 4.
        # correction 1. la reproduction n'est possible qu'à partir de 20 jours
        if self.sexe == "femelle" and self.niv_nutrition >= 2:# and self.age > 20:
            descendants.append(Coccinelle("male", 0, 0))
            descendants.append(Coccinelle("femelle", 0, 0))
            self.niv_nutrition = 0

        return descendants

    def a_survecu(self):
        """Met à jour l'âge de la coccinelle et indique si elle est encore en
        vie."""
        # Question 4.
        # correction 2. risque de 33% de mort de faim si le niveau de nutrition
        # est à 0
        #if self.niv_nutrition == 0:
        #    mort_de_faim = random.random() < 0.33
        #else:
        #    mort_de_faim = False
        self.age = self.age + 1
        return self.age < self.esperance_de_vie #and not mort_de_faim

    def __repr__(self):
        return f"Coccinelle {self.sexe}, âge: {self.age}/{self.esperance_de_vie}, niv_nutrition: {self.niv_nutrition}"


def evolution(population, nb_proies):
    """Simule une journée dans l'écosystème :
    - chasse des coccinelles
    - reproduction
    - vieillissement et mortalité
    - croissance des pucerons

    population est une liste d'instances de la classe Coccinelle
    nb_proies est un entier indiquant le nombre de proies

    Cette fonction renvoie un couple (population_suivante, nouveau_nb_proies)
    indiquant la nouvelle population à la fin de la journée et le nombre de
    proies."""
    population_suivante = []
    nouveau_nes = []
    nb_coccinelles = len(population)

    for coccinelle in population:
        nb_proies = coccinelle.chasser(nb_proies, nb_coccinelles)

        if coccinelle.a_survecu():
            population_suivante.append(coccinelle)

        nouveau_nes += coccinelle.reproduction()

    # Croissance naturelle des pucerons (augmentation de 20% par jour)
    nb_proies = int(nb_proies * 1.2)

    # Ajout des nouveau-nés en fin de journée
    population_suivante += nouveau_nes

    return population_suivante, nb_proies


###############################################################################
# Écrire ci-dessous le code pour les questions de l'énoncé                    #
###############################################################################

# question 1.
population = [
    Coccinelle("femelle", 10, 2),
    Coccinelle("femelle", 10, 2),
    Coccinelle("male", 10, 2)
]
print("\nSimulation 1\n")
nb_proies = 200
for i in range(1, 6):
    population, nb_proies = evolution(population, nb_proies)
    print(f"Fin du jour {i} \t coccinelles: {len(population)}, \t pucerons: {nb_proies}")

# question 2.
def simulation_simple(population, nb_proies):
    i = 0
    while i < 30 and len(population) > 0 and nb_proies > 0:
        i += 1
        population, nb_proies = evolution(population, nb_proies)
        print(f"Fin du jour {i} \t coccinelles: {len(population)}, \t pucerons: {nb_proies}")

print("\nSimulation 2\n")
simulation_simple(population, 1000)

# question 3. (voir documentation dans la classe Coccinelle)

# Question 4. (voir ajouts aux méthodes reproduction et a_survecu)
