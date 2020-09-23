import numpy as np

def findPrimes():
    primes = np.array([])
    n = 0
    i = 3
    z = 0
    g = 0
    while n==0:
        for p in range(2, i):
            if i%p==0:
                i+=1
                break
            else:
                p+=1
            if p == i:
                primes = np.append(primes, i)
                i+=1
                print(primes.size)
                g = 0
            if primes.size==10002:
                n+=1
        if primes.size % 1000 == 0 and g==0:
            z = z + 10
            print("Progress- ", z, "%")
            g+=1

    print("The 10001st prime number is: ", primes[10001])

findPrimes()

