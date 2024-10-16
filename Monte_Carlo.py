# Modules
import numpy as np
import itertools
from random import randint

# Paramètres initiaux
n = 10 #taille du système
B = 0.2 #champ magnétique adimensionné
T = 0.1 #température adimensionnée
k = 100 #nombre d'étapes

dic_voisins = {}
for i in range(n):
	for j in range(n):
		dic_voisins[(i,j)] = []
		liste_voisins_i, liste_voisins_j = [], []
		if -1 < i-1 < n:
			liste_voisins_i.append(i-1)
		if -1 < i+1 < n:
			liste_voisins_i.append(i+1)
		if -1 < j-1 < n:
			liste_voisins_j.append(j-1)
		if -1 < j+1 < n:
			liste_voisins_j.append(j+1)
		for voisin_i in liste_voisins_i:
			dic_voisins[(i,j)].append((voisin_i, j))
		for voisin_j in liste_voisins_j:
			dic_voisins[(i,j)].append((i, voisin_j))

# Fonctions auxiliaires
def énergie(tab_config):
	E_tot = 0
	for i in range(n):
		for j in range(n):
			E_tot -= B*tab_config[i, j]
			for (k,l) in dic_voisins[(i,j)]:
				E_tot += 0.5*tab_config[k,l]
	return E_tot
	
def moment(
	
# Algorithme
## Initialisation
tab_config = np.ones(n)
for dipôle in tab_config:
	if randint(0, 1):
		dipôle = -1

## Itération : on parcourt l'espace des états accessibles
liste_énergies = []
for i in range(k):
	
