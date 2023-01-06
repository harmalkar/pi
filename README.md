# pi
This code is meant to serve as an introduction to Python, as well as an introduction to Monte Carlo methods. 

By throwing darts randomly at a square with a circular dartboard inscribed in it, you can quickly estimate the value of π:

<p align="center">
<img src="https://github.com/harmalkar/pi/blob/master/movie.gif?raw=true"></img>
</p>

This works because [the area of the circle is related to the area of the square by a factor of π/4](https://www.geeksforgeeks.org/estimating-value-pi-using-monte-carlo), so the probability of a random dart landing within the circle is π/4. Therefore, as we throw more darts on the board and measure how many darts land in the cirle, we can take the ratio of (number of darts landing in the circle) / (total darts) and multiply it by 4 to get an estimate of π 
