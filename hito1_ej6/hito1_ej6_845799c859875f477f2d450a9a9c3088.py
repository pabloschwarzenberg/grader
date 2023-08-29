#Ordenar tres números

n1 = int(input("Ingresa un número: "))
n2 = int(input("Ingresa un número: "))
n3 = int(input("Ingresa un número: "))

if n1 == n2 and n1 < n3:
    print(n1,n2,n3)
elif n1 == n2 and n3 < n1:
    print(n3,n2,n1)
elif n1 == n3 and n1 < n2:
    print(n1,n3,n2)
elif n1 == n3 and n2 < n1:
    print(n2,n1,n3)
elif n2 == n3 and n2 < n1:
    print(n3,n2,n1)
elif n2 == n3 and n1 < n2:
    print(n1,n2,n3)
elif n1 == n2 and n1 == n3:
    print(n1,n2,n3)
elif n1 < n2 and n2 < n3:
    print(n1,n2,n3)
elif n1 < n3 and n3 < n2:
    print(n1,n3,n2)
elif n2 < n1 and n1 < n3:
    print(n2,n1,n3)
elif n2 < n3 and n3 < n1:
    print(n2,n3,n1)
elif n3 < n2 and n2 < n1:
    print(n3,n2,n1)
elif n3 < n1 and n1 < n2:
    print(n3,n1,n2)
elif n1 == n3 and n2 < n1:
    print(n2,n1,n1)
elif n1 == n3 and n2 > n1:
    print(n1,n1,n2)