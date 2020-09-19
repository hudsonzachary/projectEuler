def prime_finder(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                # this is not prime
                break
        else:
            # is a prime number
            return x


def prime_sum(x):
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


    print(sum_primes)


def circular_primes():
    circle_primes = []
