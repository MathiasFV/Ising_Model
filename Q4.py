from Monte_Carlo import *
		
def Question_4(T, nb_pas_MC, B_min, B_max, n):
	energies = []
	moments = []
	capacites = []
	
	champs = np.linspace(B_min, B_max, 10)
	
	for B in champs:
		print('B =',B)
		E, C, M = Monte_Carlo(T,nb_pas_MC,B, n)
		energies.append(E)
		moments.append(M)
		capacites.append(C)

	fig, ax = plt.subplots(3,1, sharex=True, figsize=(10,9))
	fig.tight_layout(h_pad=2, w_pad=2)
    

    # Tracé de l'énergie
	ax[0].plot(champs, energies)
	ax[0].set_ylabel('$E$')
 #   ax[0].set_yscale('log')
	ax[0].grid(visible=True, which="both")

    # Tracé du moment magnétique
	ax[1].plot(champs, moments, color='green')
	ax[1].set_ylabel(r'$\mu$')
	ax[1].grid(visible=True, which="both")
#    ax[1].set_yscale('log')

	# Tracé de la capacité thermique
	ax[2].plot(champs, capacites, color='orange')
	ax[2].set_ylabel('$c_v$')
	ax[2].set_xlabel('B')
	ax[2].grid(visible=True, which="both")
	ax[2].set_yscale('log')

	plt.tight_layout()
	plt.savefig('Figures/Q3_nb_pas_MC='+str(nb_pas_MC)+'_T='+str(T)+'_n='+str(n)+'.pdf', bbox_inches="tight")
	plt.close()
	
Question_4(T=1, nb_pas_MC=50000, B_min=0.1, B_max=5, n=10)
