import numpy as np
import matplotlib.pyplot as plt
from random import randint, random
from numpy import mean

# Fonctions auxiliaires
def énergie(tab_config,dic_voisins,B):
	n = len(tab_config[0])
	E_tot = 0
	for i in range(n):
		for j in range(n):
			E_tot -= B*tab_config[i, j]
			for (k,l) in dic_voisins[(i,j)]:
				E_tot += 0.5*tab_config[k,l]*tab_config[i, j]
	return E_tot

def moment(tab_config):
	n = len(tab_config[0])
	liste_mu = []
	for i in range(n):
		for j in range(n):
			liste_mu.append(tab_config[i, j])
	return mean(liste_mu)

#def capacité_thermique(tab_config, dic_voisins, T, B):
#	n = len(tab_config[0])
#	liste_E = []
#	for i in range(n):
#		for j in range(n):
#			E = -B*tab_config[i, j]
#			for (k,l) in dic_voisins[(i,j)]:
#				E += 0.5*tab_config[k,l]*tab_config[i, j]
#			liste_E.append(E)
#	return np.var(liste_E)/(T**2)

# Algorithme Monte Carlo

def Monte_Carlo(T,nb_pas_MC,B, n):
	## Initialisation
	tab_config = np.ones((n, n))
	for i in range(n):
		for j in range(n):
			if randint(0, 1):
				tab_config[i, j] = -1
	
	dic_voisins = {}
	for i in range(n):
		for j in range(n):
			dic_voisins[(i, j)] = []
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
				dic_voisins[(i, j)].append((voisin_i, j))
			for voisin_j in liste_voisins_j:
				dic_voisins[(i, j)].append((i, voisin_j))
   
	liste_énergies = []
	liste_capacités_thermiques = []
	liste_moments = []

	## Itération : on parcourt l'espace des états accessibles
	for pas in range(nb_pas_MC):
		i = randint(0, n - 1) # Choix aléatoire d'un état à proposer à la modification
		j = randint(0, n - 1)
		delta_mu = -2*tab_config[i, j]
		delta_E = -B*delta_mu
		for (k, l) in dic_voisins[(i, j)]:
			delta_E += 0.5*delta_mu*tab_config[k, l]
		if delta_E < 0:
			tab_config[i, j] *= -1 # Le changement est systématiquement accepté s'il induit une baisse de l'énergie du système.
		else:
			P = np.exp(-delta_E/T)
			if random() < P: # Sinon, il peut être accepté ou refusé selon une probabilité décroissant avec l'augmentation de l'énergie qu'il induit.
				tab_config[i, j] *= -1
		if pas > nb_pas_MC/2:
			liste_énergies.append(énergie(tab_config,dic_voisins,B))
			liste_moments.append(moment(tab_config))
	
	capacité_thermique = np.var(liste_énergies)/(T**2)

	return np.mean(liste_énergies), capacité_thermique, np.mean(liste_moments)


def Monte_Carlo_evolution(T,liste_nb_pas_MC,B, n):

	liste_nb_pas_MC = [int(nb_pas_MC) for nb_pas_MC in liste_nb_pas_MC]
	nb_pas_MC = liste_nb_pas_MC[-1]

	## Initialisation
	tab_config = np.ones((n, n))
	for i in range(n):
		for j in range(n):
			if randint(0, 1):
				tab_config[i, j] = -1
	
	dic_voisins = {}
	for i in range(n):
		for j in range(n):
			dic_voisins[(i, j)] = []
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
				dic_voisins[(i, j)].append((voisin_i, j))
			for voisin_j in liste_voisins_j:
				dic_voisins[(i, j)].append((i, voisin_j))
   
	liste_énergies = []
#	liste_capacités_thermiques = []
	liste_moments = []
	
	liste_energies_evolution = []
	liste_capacités_thermiques_évolution = []
	liste_moments_évolution = []

	## Itération : on parcourt l'espace des états accessibles
	for pas in range(nb_pas_MC+1):
		i = randint(0, n - 1) # Choix aléatoire d'un état à proposer à la modification
		j = randint(0, n - 1)
		delta_mu = -2*tab_config[i, j]
		delta_E = -B*delta_mu
		for (k, l) in dic_voisins[(i, j)]:
			delta_E += 0.5*delta_mu*tab_config[k, l]
		if delta_E < 0:
			tab_config[i, j] *= -1 # Le changement est systématiquement accepté s'il induit une baisse de l'énergie du système.
		else:
			P = np.exp(-delta_E/T)
			if random() < P: # Sinon, il peut être accepté ou refusé selon une probabilité décroissant avec l'augmentation de l'énergie qu'il induit.
				tab_config[i, j] *= -1
		liste_énergies.append(énergie(tab_config,dic_voisins,B))
		liste_moments.append(moment(tab_config))
		
		if pas in liste_nb_pas_MC:
			print('pas', pas)
			capacité_thermique = np.var(liste_énergies)/(T**2)
			liste_energies_evolution.append(mean(liste_énergies))
			liste_capacités_thermiques_évolution.append(capacité_thermique)
			liste_moments_évolution.append(mean(liste_moments))
		
	return liste_energies_evolution, liste_capacités_thermiques_évolution, liste_moments_évolution
