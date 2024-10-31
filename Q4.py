from Monte_Carlo import *
		
def Question_4(nb_pas_MC, B_min, B_max, n):
	energies = []
	moments = []
	capacites = []
	
	champs = np.linspace(B_min, B_max, 20)
	
	for B in champs:
		print('B =',B)
		E, C, M = Monte_Carlo(0.8,nb_pas_MC,B, n)
		energies.append(E)
		moments.append(M)
		capacites.append(C)

	fig, ax = plt.subplots(1,1, sharex=True, figsize=(10,3))
	fig.tight_layout(h_pad=2, w_pad=2)
    
	ax.plot(champs, capacites, color='orange')
	ax.set_ylabel(r'$c_v^{\star}$')
	ax.set_xlabel(r'$B^{\star}$')
	ax.grid(visible=True, which="both")
	ax.set_yscale('log')

	plt.tight_layout()
	plt.savefig('Figures/Q4_nb_pas_MC='+str(nb_pas_MC)+'_Bmin='+str(B_min)+'_Bmax='+str(B_max)+'_n='+str(n)+'.pdf', bbox_inches="tight")
	plt.close()
	
Question_4(nb_pas_MC=1000000, B_min=0.1, B_max=5, n=10)
