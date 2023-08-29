#Ordenar tres números
n1 = eval(input("Ingrese número1: ")) 
n2 = eval(input("Ingrese número2: "))
n3 = eval(input("Ingrese número1: "))
if n1<n2<n3:
    print(n1, ",",n2, ",",n3)
if n2<n3<n1:
    print(n2, ",",n3, ",",n1)
if n3<n1<n2:
    print(n3, ",",n1, ",",n2)
if n1<n3<n2:
    print(n1, ",",n3, ",",n2)
if n2<n1<n3:
    print(n2, ",",n1, ",",n3)
if n1==n2==n3:
    print(n1, ",",n2, ",",n3)
if n1==n2<n3:
    print(n1, ",",n2, ",",n3)
if n2==n3<n1:
    print(n2, ",",n3, ",",n1)
if n1==n3<n2:
    print(n1, ",",n3, ",",n2)
if n2<n1==n3:
    print(n2, ",",n1, ",",n3)