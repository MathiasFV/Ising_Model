import numpy as np
import matplotlib.pyplot as plt
from random import randint, random

# Paramètres initiaux
n = 10  # taille du système
B = 0.2  # champ magnétique adimensionné
T_min = 0.01  # température adimensionnée
T_max = 10  # température adimensionnée
nb_pas = 1000  # nombre d'étapes

#Paramètres Question 2
resultats_Q2= []

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

def capacité_thermique(tab_config, T):
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
tab_config = np.ones((n, n))
for i in range(n):
    for j in range(n):
        if randint(0, 1):
            tab_config[i, j] = -1

## Itération : on parcourt l'espace des états accessibles
def Monte_Carlo(T,nb_pas_MC):
    liste_énergies = []
    liste_capacités_thermiques = []
    liste_moments = []

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
        liste_énergies.append(énergie(tab_config))
        liste_moments.append(moment(tab_config))
        liste_capacités_thermiques.append(capacité_thermique(tab_config, T))

    return np.mean(liste_énergies), np.mean(liste_capacités_thermiques), np.mean(liste_moments)

# Question 1 : Vérification de la convergence des grandeurs à une température donnée
def Question_1(T, nb_iters):
    energies = []
    moments = []
    capacites = []

    iter_values = np.linspace(100, nb_iters, 10)

    for nb_iter in iter_values:
      nb_iter = int(nb_iter)
      E, C, M = Monte_Carlo(T,nb_iter)
      energies.append(E)
      moments.append(M)
      capacites.append(C)

    plt.figure(figsize=(12, 8))

    # Tracé de l'énergie
    plt.subplot(3, 1, 1)
    plt.plot(iter_values, energies, label='Énergie')
    plt.title(f"Convergence des grandeurs pour T = {T}")
    plt.ylabel('Énergie')
    plt.legend()

    # Tracé du moment magnétique
    plt.subplot(3, 1, 2)
    plt.plot(iter_values, moments, label='Moment magnétique', color='green')
    plt.ylabel('Moment')
    plt.legend()

    # Tracé de la capacité thermique
    plt.subplot(3, 1, 3)
    plt.plot(iter_values, capacites, label='Capacité Thermique', color='orange')
    plt.ylabel('Capacité thermique')
    plt.xlabel('Nombre d\'itérations')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Appel de la question 1 pour tester la convergence à une température donnée

Question_1(T=1,nb_iters=nb_pas)

# Question 2 : Évolution des grandeurs en fonction de la température
def Question_2():
    resultats_Q2 = []
    T_values = np.linspace(T_min, T_max, 100)

    for T in T_values:
        resultats_Q2.append(Monte_Carlo(T))

    resultats_Q2 = np.array(resultats_Q2)

    # Tracé des résultats
    plt.figure(figsize=(12, 8))

    # Tracé de l'énergie
    plt.subplot(3, 1, 1)
    plt.plot(T_values, resultats_Q2[:, 0], label='Énergie')
    plt.title("Évolution des grandeurs en fonction de la température")
    plt.ylabel('Énergie')
    plt.legend()

    # Tracé de la capacité thermique
    plt.subplot(3, 1, 2)
    plt.plot(T_values, resultats_Q2[:, 1], label='Capacité Thermique', color='orange')
    plt.ylabel('Capacité thermique')
    plt.legend()

    # Tracé du moment
    plt.subplot(3, 1, 3)
    plt.plot(T_values, resultats_Q2[:, 2], label='Moment magnétique', color='green')
    plt.xlabel('Température')
    plt.ylabel('Moment')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Appel de la Question 2 pour tracer les grandeurs en fonction de la température
#Question_2()
