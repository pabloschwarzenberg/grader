#Ordenar 3 numeros
n1=int(input("Ingrese numero 1: "))
n2=int(input("Ingrese numero 2: "))
n3=int(input("Ingrese numero 3: "))

if n1<=n2<=n3:
    print("El orden es: ",n1,",",n2,",",n3)

if n2<n1<n3:
    print("El orden es: ",n2,",",n1,",",n3)

if n3<=n2<=n1:
    print("El orden es: ",n3,",",n2,",",n1)

if n1<=n3<=n2:
    print("El orden es: ",n1,",",n3,",",n2)

if n2<=n3<=n1:
    print("El orden es: ",n2,",",n3,",",n1)

if n3<=n1<=n2:
    print("El orden es: ",n3,",",n1,",",n2)
