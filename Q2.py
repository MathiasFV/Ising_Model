from Monte_Carlo import *

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
	ax[1].set_ylabel(r'$\bar{\mu}$')
	ax[1].grid(visible=True, which="both")
#    ax[1].set_yscale('log')

	# Tracé de la capacité thermique
	ax[2].plot(temperatures, capacites, color='orange')
	ax[2].set_ylabel('$c_v$')
	ax[2].set_xlabel('T')
	ax[2].grid(visible=True, which="both")
	ax[2].set_yscale('log')

	plt.tight_layout()
	plt.savefig('Figures/Q2_nb_pas_MC='+str(nb_pas_MC)+'_T='+str(T)+'_B='+str(B)+'_n='+str(n)+'.pdf', bbox_inches="tight")
	plt.close()
	
Question_2(T_min=0.1, T_max=5, nb_pas_MC=100000, B=0, n=20)
