n1 = eval(input("Ingrese numero 1: "))
n2 = eval(input("Ingrese numero 2: "))
n3 = eval(input("Ingrese numero 3: "))


if n1 < n2 and n2 < n3:
    print(n1,",",n2,",",n3)
if n1 < n3 and n2 > n3:
    print(n1,",",n3,",",n2)


if n2 < n1 and n1 < n3:
    print(n2,",",n1,",",n3)
if n2 < n3 and n1 > n3:
    print(n2,",",n3,",",n1)



if n3 < n2 and n2 < n1:
    print(n3,",",n2,",",n1)
if n3 < n1 and n2 > n1:
    print(n3,",",n1,",",n2)


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