import time
import array
import math

x = 600851475143
y = int

#while i > 0:
#    y -= 1
#    i -= 1
#    print(y)
#    if x%y==0:
#        print("Got a chance!")
#        r = y
#        t = y
#        while r > 0:
#            r -= 1
#            if t%r==0:
#                print("We've got a match!")
#                print(r)


def primeFactorFinder(i):
    while i%2==0:
        print(2)
        n = n/2
    for n in range(3, int(math.sqrt(i))+1, 2):
        while i%n==0:
            print(n)
            i = i/n
    if i > 2:
        print(i)

i = x
primeFactorFinder(i)