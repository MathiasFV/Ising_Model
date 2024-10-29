from Monte_Carlo import *


# Question 1 : Vérification de la convergence des grandeurs à une température donnée
def Question_1(T, nb_pas_MC_max, B, n):
	energies = []
	moments = []
	capacites = []

	iter_values = np.linspace(100, nb_pas_MC_max, 20)

	for nb_pas_MC in iter_values:
		print('nb_pas_MC = ',nb_pas_MC)
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
	plt.savefig('Figures/Q1_T='+str(T)+'_nb_pas_MC_max='+str(nb_pas_MC_max)+'_B='+str(B)+'_n='+str(n)+'.pdf', bbox_inches="tight")
	plt.close()
	
Question_1(T=10,nb_pas_MC_max=200000,B = 0.2, n=10)
