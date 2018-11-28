import math

def squareRoot(num,precision_digit=3):
	x0 = num+0.1
	tolerance = 0.0000000001
	x = x0
	for i in range(1000):
		x = (x + num/x)/2
		if (x*x-num)<tolerance:
			return round(x,precision_digit)
	return x

print("square root by built-in math: ")
print(math.sqrt(0.121212121))
print("square root by iteration: ")
print(squareRoot(0.121212121))



