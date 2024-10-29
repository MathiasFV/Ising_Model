from Monte_Carlo import *
		
def Question_4(nb_pas_MC, B_min, B_max, n):
	energies = []
	moments = []
	capacites = []
	
	champs = np.linspace(B_min, B_max, 10)
	
	for B in champs:
		print('B =',B)
		E, C, M = Monte_Carlo(1,nb_pas_MC,B, n)
		energies.append(E)
		moments.append(M)
		capacites.append(C)

	fig, ax = plt.subplots(1,1, sharex=True, figsize=(10,3))
	fig.tight_layout(h_pad=2, w_pad=2)
    

	ax.plot(champs, capacites, color='orange')
	ax.set_ylabel('$c_v$')
	ax.set_xlabel('B')
	ax.grid(visible=True, which="both")
	ax.set_yscale('log')

	plt.tight_layout()
	plt.savefig('Figures/Q4_nb_pas_MC='+str(nb_pas_MC)+'_Bmin='+str(B_min)+'_Bmax='+str(B_max)+'_n='+str(n)+'.pdf', bbox_inches="tight")
	plt.close()
	
Question_4(nb_pas_MC=50000, B_min=0.1, B_max=5, n=10)
