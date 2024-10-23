import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from random import randint, random

# Paramètres initiaux
T_min = 0.01  # température adimensionnée
T_max = 10  # température adimensionnée


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
	mu_tot = 0
	for i in range(n):
		for j in range(n):
			mu_tot += tab_config[i, j]
	return mu_tot

def capacité_thermique(tab_config, dic_voisins, T, B):
	n = len(tab_config[0])
	liste_E = []
	for i in range(n):
		for j in range(n):
			E = -B*tab_config[i, j]
			for (k,l) in dic_voisins[(i,j)]:
				E += 0.5*tab_config[k,l]*tab_config[i, j]
			liste_E.append(E)
	return np.var(liste_E)/(T**2)

# Algorithme

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
		i = randint(0, n - 1)
		j = randint(0, n - 1)
		delta_mu = -2*tab_config[i, j]
		delta_E = -B*delta_mu
		for (k, l) in dic_voisins[(i, j)]:
			delta_E += delta_mu*tab_config[k, l]
		if delta_E < 0:
			tab_config[i, j] *= -1
		else:
			P = np.exp(-delta_E/T)
			if random() < P:
				tab_config[i, j] *= -1
		liste_énergies.append(énergie(tab_config,dic_voisins,B))
		liste_moments.append(moment(tab_config))
		liste_capacités_thermiques.append(capacité_thermique(tab_config, dic_voisins, T,B))

	return np.mean(liste_énergies), np.mean(liste_capacités_thermiques), np.mean(liste_moments)

# Question 1 : Vérification de la convergence des grandeurs à une température donnée
def Question_1(T, nb_pas_MC_max, B, n):
	energies = []
	moments = []
	capacites = []

	iter_values = np.linspace(100, nb_pas_MC_max, 20)

	for nb_pas_MC in iter_values:
		nb_pas_MC = int(nb_pas_MC)
		E, C, M = Monte_Carlo(T,nb_pas_MC,B, n)
		energies.append(E)
		moments.append(M)
		capacites.append(C)

	fig, ax = plt.subplots(3,1, sharex=True, figsize=(10,9))
	fig.tight_layout(h_pad=2, w_pad=2)
    

    # Tracé de l'énergie
	ax[0].plot(iter_values, energies, label='Énergie')
	ax[0].set_title(f"Convergence des grandeurs pour T = {T}")
	ax[0].set_ylabel('$E$')
 #   ax[0].set_yscale('log')
	ax[0].grid(visible=True, which="both")
	ax[0].legend()

    # Tracé du moment magnétique
	ax[1].plot(iter_values, moments, label='Moment magnétique', color='green')
	ax[1].set_ylabel(r'$\mu$')
	ax[1].grid(visible=True, which="both")
#    ax[1].set_yscale('log')
	ax[1].legend()

	# Tracé de la capacité thermique
	ax[2].plot(iter_values, capacites, label='Capacité Thermique', color='orange')
	ax[2].set_ylabel('$c_v$')
	ax[2].set_xlabel('Nombre d\'itérations')
	ax[2].grid(visible=True, which="both")
	ax[2].set_yscale('log')
	ax[2].legend()

	plt.tight_layout()
	plt.savefig('Q1.pdf', bbox_inches="tight")
	plt.close()
	
def Question_2(T_min, T_max, nb_pas_MC, B, n):
	energies = []
	moments = []
	capacites = []
	
	temperatures = np.linspace(T_min, T_max, 10)
	
	for T in temperatures:
		print('T =',T)
		E, C, M = Monte_Carlo(T,nb_pas_MC,B, n)
		energies.append(E)
		moments.append(M)
		capacites.append(C)

	fig, ax = plt.subplots(3,1, sharex=True, figsize=(10,9))
	fig.tight_layout(h_pad=2, w_pad=2)
    

    # Tracé de l'énergie
	ax[0].plot(temperatures, energies)
	ax[0].set_ylabel('$E$')
 #   ax[0].set_yscale('log')
	ax[0].grid(visible=True, which="both")

    # Tracé du moment magnétique
	ax[1].plot(temperatures, moments, color='green')
	ax[1].set_ylabel(r'$\mu$')
	ax[1].grid(visible=True, which="both")
#    ax[1].set_yscale('log')

	# Tracé de la capacité thermique
	ax[2].plot(temperatures, capacites, color='orange')
	ax[2].set_ylabel('$c_v$')
	ax[2].set_xlabel('T')
	ax[2].grid(visible=True, which="both")
	ax[2].set_yscale('log')

	plt.tight_layout()
	plt.savefig('Q2.pdf', bbox_inches="tight")
	plt.close()
		


#Question_1(T=1,nb_pas_MC_max=50000,B = 0.2, n=10)
Question_2(T_min=0.1, T_max=10, nb_pas_MC=50000, B=0.2, n=10)
