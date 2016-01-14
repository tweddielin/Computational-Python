import time


def bisection(x):
	tic = time.clock()
	#x = float(raw_input("Enter a number\n"))
	epsilon = 0.01
	numGuess = 0
	low = 0.0
	high = max(1.0,x)
	ans = (high + low)/2.0
	while abs(ans**2 - x) >= epsilon:
		print 'low = ', low, 'high = ', high, 'ans = ', ans
		numGuess += 1
		if ans**2 < x:
			low = ans
		else:
			high = ans

		ans = (high + low)/2.0
		toc = time.clock()
	print 'numGuess = ', numGuess
	print ans, 'is close to square root of ', x
	print 'cost time ', toc - tic , 's\n'

def newton(x, power):
	tic = time.clock()
	#x = float(raw_input("Enter a number\n"))
	epsilon = 0.01
	numGuess = 0

	guess = x / power
	while abs(guess**power) - x) >= epsilon:
		numGuess +=1
		guess = guess - (guess**power - x) / power*guess
		print numGuess
	toc = time.clock()
	print 'Iteration numbers: ', numGuess
	print 'Square root of ', x, 'is about', guess
	print 'cost ', toc - tic, 's\n'

if __name__ == '__main__':
	#bisection()
	newton(9,3)


