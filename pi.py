# Calculating pi
import random
import matplotlib.pyplot as plt

R = 10		# radius of circle
N = 200		# number of darts
def main():
	ratio = 0.0
	for i in range(N):
		x, y = throw_dart()
		plt.plot(x,y,'b*')
		if in_circle(x, y):
			ratio += 1

	ratio /= N
	print(ratio)
	print(4*ratio)
	plt.title('Estimating pi by throwing darts')
	plt.show()

def throw_dart():
	return (random.uniform(-1*R,R), random.uniform(-1*R, R))

def in_circle(x, y):
	return x**2 + y**2 < R**2

if __name__ == "__main__":
	main()
