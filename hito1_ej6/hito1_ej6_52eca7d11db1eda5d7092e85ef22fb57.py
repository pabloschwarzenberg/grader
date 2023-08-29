#Ordenar tres números
n1 = eval(input("Ingrese numero 1: "))
n2 = eval(input("Ingrese numero 2: "))
n3 = eval(input("Ingrese numero 3: "))

#Numeros distintos

# N1

if n1 < n2 and n2 < n3:
    print(n1,",",n2,",",n3)
if n1 < n3 and n2 > n3:
    print(n1,",",n3,",",n2)

# N2

if n2 < n1 and n1 < n3:
    print(n2,",",n1,",",n3)
if n2 < n3 and n1 > n3:
    print(n2,",",n3,",",n1)

#N3

if n3 < n2 and n2 < n1:
    print(n3,",",n2,",",n1)
if n3 < n1 and n2 > n1:
    print(n3,",",n1,",",n2)

#N Iguales

if n1 == n2 and n2 < n3:
    print(n1,",",n2,",",n3)
if n1 == n2 and n2 > n3:
    print(n3,",",n2,",",n1)
if n1 == n3 and n3 < n2:
    print(n1,",",n3,",",n2)
if n1 == n3 and n3 > n2:
    print(n2,",",n3,",",n1)
if n3 == n2 and n2 < n1:
    print(n3,",",n2,",",n1)
if n3 == n2 and n2 > n1:
    print(n1,",",n2,",",n3)