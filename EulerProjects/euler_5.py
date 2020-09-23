
def smallestMultiple():
    i = 0
    x = 1
    while i==0:
        if x%20==0:
            if x%19==0:
                if x%18==0:
                    if x%17==0:
                        if x%16==0:
                            if x%15==0:
                                if x%14==0:
                                    if x%13==0:
                                        if x%12==0:
                                            if x%11==0:
                                                if x%10==0:
                                                    if x%9==0:
                                                        if x%8==0:
                                                            if x%7==0:
                                                                if x%6==0:
                                                                    if x%5==0:
                                                                        if x%4==0:
                                                                            if x%3==0:
                                                                                if x%2==0:
                                                                                    print(x," Is divisible by 1-20!")
                                                                                    i+=1
                                                                                else:
                                                                                    x += 1
                                                                            else:
                                                                                x += 1
                                                                        else:
                                                                            x += 1
                                                                    else:
                                                                        x += 1
                                                                else:
                                                                    x += 1
                                                            else:
                                                                x += 1
                                                        else:
                                                            x += 1
                                                    else:
                                                        x += 1
                                                else:
                                                    x += 1
                                            else:
                                                x += 1
                                        else:
                                            x += 1
                                    else:
                                        x += 1
                                else:
                                    x += 1
                            else:
                                x += 1
                        else:
                            x += 1
                    else:
                        x += 1
                else:
                    x += 1
            else:
                x+=1
        else:
            x+=1

def fastSmallest():
    x = 1
    i = 1
    n = 0
    while n==0:
        for i in range(1,21):
            y = i
            if x%y==0:
                i+=1
            elif x%y!=0:
                x+=1
                i = 1
            if x==232792560:
                print(x)
                n+=1

fastSmallest()