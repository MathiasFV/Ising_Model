from Monte_Carlo import *

def Question_2(T_min, T_max, nb_pas_MC, B, n):
	energies = []
	moments = []
	capacites = []
	
	temperatures = np.linspace(T_min, T_max, 30)
	
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
	ax[0].set_ylabel('$E^{\star}$')
 #   ax[0].set_yscale('log')
	ax[0].grid(visible=True, which="both")

    # Tracé du moment magnétique
	ax[1].plot(temperatures, moments, color='green')
	ax[1].set_ylabel(r'$\bar{\mu^{\star}}$')
	ax[1].grid(visible=True, which="both")
#    ax[1].set_yscale('log')

	# Tracé de la capacité thermique
	ax[2].plot(temperatures, capacites, color='orange')
	ax[2].set_ylabel(r'$c_v^{\star}$')
	ax[2].set_xlabel(r'$T^{\star}$')
	ax[2].grid(visible=True, which="both")
#	ax[2].set_yscale('log')

	plt.tight_layout()
	plt.savefig('Figures/Q2_nb_pas_MC='+str(nb_pas_MC)+'_Tmin='+str(T_min)+'_Tmax='+str(T_max)+'_B='+str(B)+'_n='+str(n)+'.pdf', bbox_inches="tight")
	plt.close()
	
Question_2(T_min=0.5, T_max=2, nb_pas_MC=1000000, B=0, n=20)
