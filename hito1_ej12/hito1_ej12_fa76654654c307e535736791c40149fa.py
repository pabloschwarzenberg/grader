import random
x=random.randrange(1, 21)
a=int(input())
if a==x:
    print("Adivinaste, mi numero era", x)
else:
    if a<x:
        print ("Mi numero es mayor")
    else:
        print ("Mi numero es menor")
    b=int(input())
    if b==x:
        print("Adivinaste, mi numero era", x)
    else:
        if b<x:
            print ("Mi numero es mayor")
        else:
            print ("Mi numero es menor")
        c=int(input())
        if c==x:
            print("Adivinaste, mi numero era", x)
        else:
            if c<x:
                print ("Mi numero es mayor")
            else:
                print ("Mi numero es menor")
            d=int(input())
            if d==x:
                print("Adivinaste, mi numero era", x)
            else:
                if d<x:
                    print ("Mi numero es mayor")
                else:
                    print ("Mi numero es menor")
                e=int(input())
                if e==x:
                    print("Adivinaste, mi numero era", x)
                else:
                    print("No adivinaste, mi numero era", x)
