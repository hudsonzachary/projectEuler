x = int
y = int

x = 1
y = 2
z = 0

for i in range(10000):
        if x%2 == 0:
            z = z + x
        elif y%2 == 0:
            z = z + y
        elif x > 4000000 or y > 4000000:
            break

        x = x + y
        y = x + y

        print(x)
        print(y)
        i += 1
        print(z)
        print("")



print(z)