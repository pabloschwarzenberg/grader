#Ordenar tres números
a = int(input("ingrese un numero"))
b = int(input("ingrese un numero"))
c = int(input("ingrese un numero"))
if a<b and a<c: 
    if b<c:
        print("ordenados de menor a mayor son:",a,",",b,",",c)
    else:
        print("ordenados de menor a mayors son:",a,",",c,",",b)
if b<a and b<c:
    if a<c:
        print("ordenados de menor a mayor son",b,",",a,",",c,)
    else:
        print("ordenados de menor a mayor son",b,",",c,",",a)
if c<a and c<b:
    if a<b:
        print("ordenados de menor a mayor son:",c,",",a,",",b)
    else:
        print("ordenados de menor a mayor son:",c,",",b,",",a)
if a==b:
    if b<c:
        print("ordenados de menor a mayor son :",c,",",b,",",a)
    else:
        print("ordenados de menor a mayor son:",a,",",b,",",c)
if a==c:
    if c<b:
        print("ordenados de menor a mayor son:",c,",",a,",",b)
    else:
        print("ordenados de menor a mayor son:",a,",",c,",",b)

    