import time
import math

def prime_finder(x):
    if x > 1:
        for i in range(2, int(x/2)):
            if x % i == 0:
                # this is not prime
                break
        else:
            # is a prime number
            return x


'''def prime_sum(x):
    sum_primes = 0
    progress = 20000
    for i in range(x):
        a = prime_finder(i)
        if type(a) == int:
            sum_primes = sum_primes + a
        elif progress == i:
            print(progress / 20000)
            progress = progress + 20000
        else:
            continue

    print(sum_primes)'''


def rotate(x):
    x = str(x)
    length = len(x)
    x = x[length - 1] + x[0:length - 1]
    x = str(x)
    return x


'''def search(number_list, number):
    for i in range(len(number_list)):
        if number_list[i] == number:
            return True
    return False'''


'''def circular_primes(x):
    number_primes = 0
    circle_primes = []
    for i in range(1, x, 2):
        if type(prime_finder(i)) == int:
            prime_string = str(i)
            p = 0
            for n in range(len(prime_string)):
                temp_rotate = rotate(i)
                z = prime_finder(temp_rotate)
                if search(circle_primes, temp_rotate) == True:
                    number_primes += 1
                    break
                if p == len(prime_string) - 1:
                    number_primes += 1
                elif type(z) == int:
                    p += 1
                    circle_primes.append(temp_rotate)
                    circle_primes.sort()
    print(number_primes+1)'''


def simpleSieve(sieveSize):
    #creating Sieve.
    sieve = [True] * (sieveSize+1)
    # 0 and 1 are not considered prime.
    sieve[0] = False
    sieve[1] = False
    for i in range(2,int(math.sqrt(sieveSize))+1):
        if sieve[i] == False:
            continue
        for pointer in range(i**2, sieveSize+1, i):
            sieve[pointer] = False
    # Sieve is left with prime numbers == True
    primes = []
    for i in range(sieveSize+1):
        if sieve[i] == True:
            primes.append(i)
    return primes

def circular_primes(x):
    prime_list = simpleSieve(x)
    first_rotate = []
    second_rotate = []
    third_rotate = []
    fourth_rotate = [2, 5]
    fifth_rotate = []
    sixth_rotate = []
    seventh_rotate = []
    eighth_rotate = []
    ninth_rotate = []
    tenth_rotate = []

    for i in range(len(prime_list)):
        prime_list[i] = rotate(prime_list[i])
        if int(prime_list[i]) % 2 == 0 or int(prime_list[i]) % 5 == 0:
            continue
        else:
            first_rotate.append(prime_list[i])
    print(first_rotate)

    for i in range(len(first_rotate)):
        first_rotate[i] = rotate(first_rotate[i])
        if int(first_rotate[i]) % 2 == 0 or int(first_rotate[i]) % 5 == 0:
            continue
        else:
            second_rotate.append(first_rotate[i])
    print(second_rotate)

    for i in range(len(second_rotate)):
        second_rotate[i] = rotate(second_rotate[i])
        if int(second_rotate[i]) % 2 == 0 or int(second_rotate[i]) % 5 == 0:
            continue
        else:
            third_rotate.append(second_rotate[i])
    print(third_rotate)

    for i in range(len(third_rotate)):
        third_rotate[i] = rotate(third_rotate[i])
        if int(third_rotate[i]) % 2 == 0 or int(third_rotate[i]) % 5 == 00:
            continue
        else:
            fourth_rotate.append(third_rotate[i])
    print(fourth_rotate)

    for i in range(len(fourth_rotate)):
        fourth_rotate[i] = rotate(fourth_rotate[i])
        if type(prime_finder(int(fourth_rotate[i]))) == int:
            fifth_rotate.append(fourth_rotate[i])
    print(fifth_rotate)

    for i in range(len(fifth_rotate)):
        fifth_rotate[i] = rotate(fifth_rotate[i])
        if type(prime_finder(int(fifth_rotate[i]))) == int:
            sixth_rotate.append(fifth_rotate[i])
    print(sixth_rotate)

    for i in range(len(sixth_rotate)):
        sixth_rotate[i] = rotate(sixth_rotate[i])
        if type(prime_finder(int(sixth_rotate[i]))) == int:
            seventh_rotate.append(sixth_rotate[i])
    print(seventh_rotate)

    for i in range(len(seventh_rotate)):
        seventh_rotate[i] = rotate(seventh_rotate[i])
        if type(prime_finder(int(seventh_rotate[i]))) == int:
            eighth_rotate.append(seventh_rotate[i])
    print(eighth_rotate)

    for i in range(len(eighth_rotate)):
        eighth_rotate[i] = rotate(eighth_rotate[i])
        if type(prime_finder(int(eighth_rotate[i]))) == int:
            ninth_rotate.append(eighth_rotate[i])
    print(ninth_rotate)

    for i in range(len(ninth_rotate)):
        ninth_rotate[i] = rotate(ninth_rotate[i])
        if type(prime_finder(int(ninth_rotate[i]))) == int:
            tenth_rotate.append(ninth_rotate[i])
    print(tenth_rotate)

    print("")
    print(len(tenth_rotate))

start_time = time.time()
circular_primes(1000000)
print(time.time() - start_time)

'''start_time = time.time()
sieves(100000)
print(time.time() - start_time)'''

'''start_time = time.time()
simpleSieve(1000000)
print(time.time() - start_time)'''