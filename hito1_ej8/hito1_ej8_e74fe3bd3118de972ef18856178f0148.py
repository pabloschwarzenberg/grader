x = (input("Ingrese un número: "))

if len(x)==4:
    
    n1 = int(x[0:1])
    n2 = int(x[1:2])
    n3 = int(x[2:3])
    n4 = int(x[3:4])
    print(n1,"M +", n2,"C +", n3,"D +", n4,"U")
elif len(x)==3:
    n1 = int(x[0:1])
    n2 = int(x[1:2])
    n3 = int(x[2:3])
    print(n1,"C +", n2,"D +", n3,"U")
elif len(x)==2:
    n1 = int(x[0:1])
    n2 = int(x[1:2])
    print(n1,"D +", n2,"U")
elif len(x)==1:
    n1 = int(x[0:1])
    print(n1,"U")