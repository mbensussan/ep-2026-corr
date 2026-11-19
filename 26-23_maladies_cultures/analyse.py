import matplotlib.pyplot as plt

from transmission import Transmission

# Extraction des données

with open("./data.txt", "r") as f:
	trames = f.read().split("\n")
	trames.pop() # La dernière ligne est vide, on la supprime
	
# Création des listes de températures et d'humidités

transmissions = [Transmission(t) for t in trames]

temperatures = [t.temperature for t in transmissions if t.est_valide()]
humidites = [t.humidite for t in transmissions if t.est_valide()]

print(len(temperatures))
# Affichage des températures

plt.plot(temperatures)
plt.plot(humidites)
plt.show()
