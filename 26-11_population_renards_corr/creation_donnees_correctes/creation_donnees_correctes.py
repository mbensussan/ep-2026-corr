from donnees_habitats_original_foireux import zones_connues
from visualisation_pca import *
from prediction_habitat import *
import json
import random

# critères écologique permettant de prédire la présence de renard. On modifie
# ainsi les donénes originales foireuses pour que la présence ou l'absence de
# renard soit expliqué par les conditions écologiques (et non aléatoire
# comme dans les données originales foireuses)

for i in range(len(zones_connues)):
    if (zones_connues[i]['vegetation'] > 6 or \
    zones_connues[i]['densite_urbaine'] < 4) and \
    (zones_connues[i]['disponibilite_proies'] > 4 or \
    zones_connues[i]['proximite_eau'] > 6): #6 4 4 6
        zones_connues[i]['presence_renard'] = 1
    else:
        zones_connues[i]['presence_renard'] = 0

# Ajout de point abhérents proche de la donnée à placer

#visualisation(zones_connues)
#visualisation(zones_connues, composantes_principales=True)

compte = {'zones avec renards': 0, 'zones sans renards': 0}

for habitat in zones_connues:
    if habitat['presence_renard'] == 1:
        compte['zones avec renards'] += 1
    else:
        compte['zones sans renards'] += 1

print(compte)

zone_inconnue = {'vegetation': 6, 'proximite_eau': 4, 'densite_urbaine': 3, 'disponibilite_proies': 6} # 6 4 3 6

for k in range(1, 300):
    print(f'k: {k} \t Présence renards : {presence_renard(k, zone_inconnue, zones_connues)}')

import os

dossier_du_programme_execute = os.path.dirname(__file__)

with open(dossier_du_programme_execute +'/donnees_habitats.py', 'w') as f:
    f.write('zones_connues = [\n')
    for habitat in zones_connues:
        f.write('    ' + json.dumps(habitat) + ',\n')
    f.write(']\n')