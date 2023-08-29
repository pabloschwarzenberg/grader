#Ordenar tres números
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))
c = int(input("Ingrese un numero: "))

if a < b and a < c:
    if b < c:
        print("Ordenados de menor a mayor son:",a, "," , b, "," , c,)

    else:
        print("Ordenados de menor a mayor son:",a,",", c,",",b,)

if b < a and b < c:
    if a < c:
        print("Ordenados de menor a mayor son:",b,",", a,",", c,)

    else:
         print("Ordenados de menor a mayor son:",b,",", c,",", a,)

if c < a and c < b:
    if a < b:
        print("Ordenados de menor a mayor son:",c,",", b,",", a,)

    else:
         print("Ordenados de menor a mayor son:",c,",", b,",", a,)

if a == b:
    if b < c:
     print("Ordenados de menor a mayor son:",c,",", b,",", a,)

    else:
        print("Ordenados de menor a mayor son:",a,",", b,",", c,)

if a == c:
    if c < b:
     print("Ordenados de menor a mayor son:",c,",", a,",", b,)

    else:
        print("Ordenados de menor a mayor son:",a,",", c,",", b,)