# Bootstrap error estimation
# Requires python3.6 or newer for random.choice()

import random
import math

# Estimate the average values of functions of independent statistical samples, with an estimate of the error
# lst - list of values
# B - number of boostrap samples to take
# fcts - functions to be applied to list (default is just one function: take the average value of the elements in the list)
def bootstrap(lst, B=100, fcts=[lambda x,L:sum(x)/L]):
	n_elem = len(lst)
	n_fcts = len(fcts)
	samples = [[0. for j in range(B)] for i in range(n_fcts)]
	avgs = [0. for i in range(n_fcts)]
	sd_errs = [0. for i in range(n_fcts)]
	for i in range(n_fcts):
		for j in range(B):
			samples[i][j] = fcts[i](random.choices(lst, k=n_elem),n_elem)
		avgs[i] = sum(samples[i])/B	
		sd_errs[i] = math.sqrt(sum([samples[i][k]**2 for k in range(B)])/B - avgs[i]**2)
	return [[avgs[i], sd_errs[i]] for i in range(n_fcts)]
