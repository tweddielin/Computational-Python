import time
# Approximating the squart root using exhaustive enumeration
while True:
    tic = time.clock()
    x = float(raw_input("Enter a number\n"))
    epsilon = 0.01
    step = epsilon**2
    numGuess = 0 
    ans = 0.0
    while abs(ans**2 - x) >= epsilon and ans <= x:
        ans = ans + step
        numGuess = numGuess + 1
    toc = time.clock()
    print 'numGuess', numGuess
    if abs(ans**2 - x) >= epsilon:
        print 'Failed on square root of ', x
    else:
        print ans, 'is close to square root of', x
        print 'the error is', abs(ans**2-x)
        print 'cost', toc-tic, 's\n'
