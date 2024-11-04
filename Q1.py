from Monte_Carlo import *


# Question 1 : Vérification de la convergence des grandeurs à une température donnée
def Question_1(T, nb_pas_MC_max, B, n):
	energies = []
	moments = []
	capacites = []

	liste_nb_pas_MC = np.linspace(100, nb_pas_MC_max, 40)

	liste_energies_evolution, liste_capacités_thermiques_évolution, liste_moments_évolution = Monte_Carlo_evolution(T,liste_nb_pas_MC,B, n)

	fig, ax = plt.subplots(3,1, sharex=True, figsize=(10,9))
	fig.tight_layout(h_pad=2, w_pad=2)
    

    # Tracé de l'énergie
	ax[0].plot(liste_nb_pas_MC, liste_energies_evolution, label='Énergie')
#	ax[0].set_title(f"Convergence des grandeurs pour T = {T}")
	ax[0].set_ylabel(r'$E^{\star}$')
 #   ax[0].set_yscale('log')
	ax[0].grid(visible=True, which="both")
	ax[0].legend()

    # Tracé du moment magnétique
	ax[1].plot(liste_nb_pas_MC, liste_moments_évolution, label='Moment magnétique', color='green')
	ax[1].set_ylabel(r'$\bar{\mu^{\star}}$')
	ax[1].grid(visible=True, which="both")
#    ax[1].set_yscale('log')
	ax[1].legend()

	# Tracé de la capacité thermique
	ax[2].plot(liste_nb_pas_MC, liste_capacités_thermiques_évolution, label='Capacité Thermique', color='orange')
	ax[2].set_ylabel(r'$c_v^{\star}$')
	ax[2].set_xlabel('Nombre d\'itérations')
	ax[2].grid(visible=True, which="both")
	ax[2].set_yscale('log')
	ax[2].legend()

	plt.tight_layout()
	plt.savefig('Figures/Q1_T='+str(T)+'_nb_pas_MC_max='+str(nb_pas_MC_max)+'_B='+str(B)+'_n='+str(n)+'.pdf', bbox_inches="tight")
	plt.close()
	
Question_1(T=1.5,nb_pas_MC_max=1000000,B = 0.5, n=10)
