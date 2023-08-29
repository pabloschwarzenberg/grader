#Ordenar tres números
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))
if n1 < n2 < n3 or n1 == n2 == n3 or n1 == n2 < n3 or n1 < n2 == n3:
    print(n1,",",n2,",",n3)
elif n1 < n3 < n2 or n1 == n3 < n2:
    print(n1,",",n3,",",n2)
else:
    if n2 < n1 < n3 or n2 < n1 == n3:
        print(n2,",",n1,",",n3)
    elif n2 < n3 < n1 or n2 == n3 < n1:
        print(n2,",",n3,",",n1)
    else:
        if n3 < n1 < n2 or n3 < n1 == n2:
            print(n3,",",n1,",",n2)
        elif n3 < n2 < n1 or n3:
            print(n3,",",n2,",",n1)