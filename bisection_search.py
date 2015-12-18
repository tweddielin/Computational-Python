import time
while True:
    tic = time.clock()
    x = float(raw_input("Enter a number\n"))
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
