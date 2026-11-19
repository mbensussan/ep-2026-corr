from Sommet import Sommet
from Face import Face
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class Objet3D:

    """Représente un objet 3D composé de sommets, de faces et d'un nom."""

    def __init__(self):
        """Initialise un objet 3D vide."""
        self.sommets = []
        self.faces = []
        self.nom = ""

    def ajouter_sommet(self, x, y, z):
        """Ajoute un sommet à l'objet 3D."""
        self.sommets.append(Sommet(x, y, z))

    def ajouter_face(self, liste_sommets):
        """Ajoute une face à l'objet 3D."""
        self.faces.append(Face(liste_sommets))

    def __str__(self):
        """Renvoie une représentation textuelle de l'objet 3D."""
        return str({'nom': self.nom, 'sommets': len(self.sommets), 'faces': len(self.faces)})

    def afficher(self):
        """Affiche l'objet 3D à l'aide de matplotlib."""
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        f = []
        for face in self.faces:
            print(face.sommets)
            x = [(self.sommets[s-1].x, self.sommets[s-1].y, self.sommets[s-1].z)
                 for s in face.sommets]
            f.append(x)
        mesh = Poly3DCollection(f, alpha=0.4, edgecolor='black')
        ax.add_collection3d(mesh)
        plt.show()

    def exporter(self, nom_fichier):
        texte = f"o {self.nom}\n"
        for s in self.sommets:
            texte += f"v {s.x} {s.y} {s.z}\n"
        for f in self.faces:
            texte += "f " + " ".join(self.f) + "\n"
        with open(nom_fichier, 'w') as f:
            f.write(texte)

    def importer(self, nom_fichier):
        with open(nom_fichier, "r") as f:
            lignes = [ligne for ligne in f]
        lignes = [ligne.rstrip()]
        lignes = [ligne.split(' ') for ligne in lignes]
        obj = Objet3D()
        for ligne in lignes:
            if ligne[0] == 'o':
                obj.nom = ligne[1]
            elif ligne[0] == 'v':
                obj.sommets.append(ligne[1], ligne[2], ligne[3])
            elif ligne[0] == f:
                obj.faces.append(ligne[1:])
        return obj

    # Méthode à compléter à la question 2.
    def trouver_sommets_adjacents(self):
        for s1 in self.sommets:

            for s2 in self.sommets:
                pass

    # Méthode à modifier à la question 5  
    def transformer(self, rapport):
        """Applique une transformation d'échelle à l'objet 3D en modifiant
        directement ses sommets."""
        sommets = []
        for sommet in self.sommets:
            sommets.append(
                Sommet(sommet.x*rapport, sommet.y*rapport, sommet.z*rapport))
        self.sommet = sommets