import time

while True:
    tic = time.clock()
    x = float(raw_input("Enter a number\n"))
    epsilon = 0.01
    numGuess = 0
    guess = x / 2.0
    while abs(guess**2 - x) >= epsilon:
        numGuess +=1
        guess = guess - (guess**2 - x) / (2*guess)
    toc = time.clock()
    print 'Iteration numbers: ', numGuess
    print 'Square root of ', x, 'is about', guess
    print 'cost ', toc - tic, 's\n'

