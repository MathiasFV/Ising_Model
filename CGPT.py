import numpy as np

# Paramètres du modèle
J = 1  # Constante d'échange normalisée
mu = 1  # Moment magnétique normalisé
temperatures = np.linspace(0.5, 5.0, 50)  # Gamme de températures
sizes = range(5, 21, 5)  # Tailles du réseau de 5 à 20

# Fonction pour calculer l'énergie et la magnétisation d'une configuration
def calculate_energy(spins, J):
    energy = 0
    n = spins.shape[0]
    for i in range(n):
        for j in range(n):
            S = spins[i, j]
            neighbors = spins[(i+1)%n, j] + spins[i, (j+1)%n] + spins[(i-1)%n, j] + spins[i, (j-1)%n]
            energy += -J * S * neighbors
    return energy / 2  # pour éviter le double comptage

# Fonction Metropolis
def metropolis(spins, T, J):
    n = spins.shape[0]
    i, j = np.random.randint(0, n, 2)
    S = spins[i, j]
    neighbors = spins[(i+1)%n, j] + spins[i, (j+1)%n] + spins[(i-1)%n, j] + spins[i, (j-1)%n]
    dE = 2 * J * S * neighbors
    if dE < 0 or np.random.rand() < np.exp(-dE / T):
        spins[i, j] = -S
    return spins

# Simulation pour chaque taille et température
results = []
for n in sizes:
    Cv_vs_T = []
    for T in temperatures:
        spins = np.random.choice([-1, 1], (n, n))  # Initialisation aléatoire
        energy = calculate_energy(spins, J)
        energy2_sum = 0
        energy_sum = 0
        steps = 1000 * n**2
        for step in range(steps):
            spins = metropolis(spins, T, J)
            energy = calculate_energy(spins, J)
            energy_sum += energy
            energy2_sum += energy**2
        avg_energy = energy_sum / steps
        avg_energy2 = energy2_sum / steps
        Cv = (avg_energy2 - avg_energy**2) / (T**2)  # Capacité calorifique
        Cv_vs_T.append(Cv)
    results.append((n, temperatures, Cv_vs_T))

# Affichage des résultats
import matplotlib.pyplot as plt

for (n, temps, cv) in results:
    plt.plot(temps, cv, label=f'Taille {n}x{n}')
plt.xlabel("Température")
plt.ylabel("Capacité calorifique Cv")
plt.legend()
plt.title("Capacité calorifique en fonction de la température pour différentes tailles de réseau")
plt.show()
