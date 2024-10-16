# Modules
import numpy as np
import itertools
from random import randint

# Paramètres initiaux
n = 10 #taille du système
B = 0.2 #champ magnétique adimensionné
T_min = 0.1 #température adimensionnée
T_max = 10 #température adimensionnée
nb_pas = 100 #nombre d'étapes

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
				E_tot += 0.5*tab_config[k,l]*tab_config[i, j]
	return E_tot
	
def moment(tab_config):
	mu_tot = 0
	for i in range(n):
		for j in range(n):
			mu_tot += tab_config[i, j]
	return mu_tot
	
def capacité_thermique(tab_config):
	liste_E = []
	for i in range(n):
		for j in range(n):
			E = -B*tab_config[i, j]
			for (k,l) in dic_voisins[(i,j)]:
				E += 0.5*tab_config[k,l]*tab_config[i, j]
			liste_E.append(E)
	return np.var(liste_E)/(T**2)
	
# Algorithme
## Initialisation
tab_config = np.ones(n)
for dipôle in tab_config:
	if randint(0, 1):
		dipôle = -1

## Itération : on parcourt l'espace des états accessibles
liste_énergies = []
liste_capacités_thermiques = []
liste_moments = []

def Monte_Carlo(T):
	for pas in range(nb_pas):
		i = random.randint(0, n - 1)
		j = random.randint(0, n - 1)
		delta_mu = -2*tab_config[i, j]
		delta_E = -B*delta_mu
		for (k,l) in dic_voisins[(i,j)]:
			delta_E+=delta_mu*tab_config[k,l]
		if delta_E < 0 :
			tab_config[i, j]*=-1
		else:
			P = np.exp(-delta_E/T)
			if random() < P:
				tab_config[i, j]*=-1
		liste_énergies.append(énergie(tab_config))
		liste_capacités_thermiques.append(moment(tab_config))
		liste_moments.append(capacité_thermique(tab_config))
	return np.mean(liste_énergies), np.mean(liste_capacités_thermiques), np.mean(liste_moments)

"""
def Question_2():
	for T in np.linspace(T_min, T_max, 1000):
"""
