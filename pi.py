# Estimating pi with darts

import random
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
import sys
import os
import bootstrap as bs

def main():
	x = input("Enter 'movie' to generate movie, or 'stat' for statistical analysis: ")
	if x == 'movie':
		movie()
	elif x == 'stat':
		stat()
	else:
		print("Undefined input")

# N - total number of darts thrown
# R - radius of circle
# S - number of rounds for statistics
# output - output file
def stat(N = 100, R = 10, S = 100, output = 'stat.png'):
	avgs, errs = [0]*N, [0]*N

	print("Throwing darts...")
	for i in range(1,N+1):
		estimates = []
		for j in range(S):
			hits = 0.0
			for k in range(i):
				x, y = throw_dart(R)
				if in_circle(R, x, y):
					hits += 1
			estimates.append(4*hits/i)
		avgs[i-1], errs[i-1] = bs.bootstrap(estimates)[0]

	plt.title('Error in pi estimation with %d rounds of N darts vs. N' % (S))
	plt.errorbar(np.arange(1,N+1),avgs,yerr=errs, fmt='o', label = 'Estimation')
	plt.plot(np.arange(1,N+1),[3.14159]*N,'r--', label='True value')
	plt.legend()
	plt.xlabel('Number of darts thrown')
	plt.ylabel('Estimated value of pi')
	plt.savefig(output)
	print("Output saved in " + output)

# N - number of darts thrown
# R - radius of circle
# output - output movie file
def movie(N = 100, R = 10, output = 'pi.mp4'):
	hits = 0.0
	estimates = []
	errors = []
	xs = []
	ys = []

	sys.stdout.write("Throwing darts and taking pictures: ")
	for i in range(N):
		x, y = throw_dart(R)
		if in_circle(R, x, y):
			hits += 1

		# Add dart to collection
		irange = np.arange(1,i+2)
		xs.append(x)
		ys.append(y)

		# Compute estimate of pi and relative error
		estimates.append(4*hits/(i+1))
		errors.append((estimates[i] - 3.14159)/3.14159)

		# Define plot and axes
		plt.title('Estimating pi by throwing darts')
		a1 = plt.subplot2grid((3,2),(0,0), rowspan = 2, adjustable='box', aspect=1)
		a2 = plt.subplot2grid((3,2),(2,0), colspan = 2)
		a3 = plt.subplot2grid((3,2),(0,1), rowspan = 2)
			
		# Set titles
		a1.set_title('Dart Locations')
		a2.set_title('Estimated Value of Pi = 3.14159...')
		a3.set_title('Relative Error')
		
		# Plot darts
		a1.plot(xs,ys,'b*')

		# Plot circle
		delta = 0.1
		circle_x = np.arange(-R,R+delta,delta)
		a1.plot(circle_x, np.sqrt(R**2 - circle_x**2), 'r--')
		a1.plot(circle_x, -np.sqrt(R**2 - circle_x**2), 'r--')
		
		# Plot estimates
		a2.set_xlim([1,N])
		a2.plot(irange, estimates, '--')
		a2.plot(i+1, estimates[i], 'r*')
		
		# Plot pi for reference
		a2.plot(np.arange(1,N+1), [3.14159]*N, 'b--')

		# Plot error
		a3.set_xlim([1,N])
		a3.plot(irange, errors, '--')
		a3.plot(i+1, errors[i], 'y*')

		# Plot 0 for reference
		a3.plot(np.arange(1,N+1), [0]*N)
		# Save plot to png
		plt.tight_layout()
		plt.savefig('out/pi' + format(i,'02d') + '.png')
		plt.clf()
		if ((i+1)*100)/N % 10 == 0:
			sys.stdout.write(format(int(((i+1)*100)/N), '02d') + '% ')
			sys.stdout.flush()
	print()
	print("Creating video...")
	os.system('ffmpeg -r 30 -i out/pi%02d.png -vcodec libx264 -crf 25 -pix_fmt yuv420p -y -hide_banner -loglevel panic ' + output)
	print("Output saved in " + output)

def throw_dart(R):
	return (random.uniform(-1*R,R), random.uniform(-1*R, R))

def in_circle(R, x, y):
	return x**2 + y**2 < R**2

if __name__ == "__main__":
	main()
