from Monte_Carlo import *

def Question_3(T_min, T_max, nb_pas_MC):
	B = 0
	
	temperatures = np.linspace(T_min, T_max, 20)
	temperatures_bis = np.linspace(T_min, T_max, 300)
	
	fig, ax = plt.subplots(1,1, sharex=True, figsize=(10,3))
	fig.tight_layout(h_pad=2, w_pad=2)
	
	for n in [5,10,15,20]:
		print('n = ',n)
		capacites = []
		for T in temperatures:
			E, C, M = Monte_Carlo(T,nb_pas_MC,B, n)
			capacites.append(C)
			
		X_Y_Spline = make_interp_spline(temperatures, capacites)
		capacites_lissées = X_Y_Spline(temperatures_bis)

		ax.plot(temperatures_bis, capacites_lissées, label = 'n = '+str(n))
		
	ax.legend()
	ax.set_ylabel(r'$c_v^{\star}$')
	ax.set_xlabel(r'$T^{\star}$')
	ax.grid(visible=True, which="both")
	ax.set_yscale('log')

	plt.tight_layout()
	plt.savefig('Figures/Q3_log_lissage_nb_pas_MC='+str(nb_pas_MC)+'_Tmin='+str(T_min)+'_Tmax='+str(T_max)+'.pdf', bbox_inches="tight")
	plt.close()
	
Question_3(T_min=0.7, T_max=1.4, nb_pas_MC=1000000)
