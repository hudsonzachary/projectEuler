def sqsum(n):
    x=0
    for i in range(n):
        x = x + i**2
        i+=1
        print(i)
    print(x)
    return(x)

def sumsq(n):
    y = 0
    for i in range(n+1):
        y = y + i
        i+=1
        print(i)
    y = y**2
    print(y)
    return(y)

def diff():
    n = int(input("Enter the range: "))
    print("The difference is: ", sumsq(n)-sqsum(n))

diff()