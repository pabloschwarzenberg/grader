print("Ingrese 3 numeros")
n1=eval(input("Ingrese el 1er numero: "))
n2=eval(input("Ingrese el 2do numero: "))
n3=eval(input("Ingrese el 3er numero: "))
if(n1<n2<n3):
    print("El orden de menor a mayor es:",n1,n2,n3)
if(n2<n3<n1):
    print("El orden de menor a mayor es:",n2,n3,n1)
if(n2<n1<n3):
    print("El orden de menor a mayor es:",n2,n1,n3)
if(n1<n3<n2):
    print("El orden de menor a mayor es:",n1,n3,n2)
if(n3<n2<n1):
    print("El orden de menor a mayor es:",n3,n2,n1)
if(n3<n1<n2):
    print("El orden de menor a mayor es:",n1,n3,n2)
if (n1<=n2<=n3):
    print("El orden de menor a mayor es:",n1,n2,n3)
if (n2<=n3<=n1):
    print("El orden de menor a mayor es:",n2,n3,n1)
if (n2<=n1<=n3):
    print("El orden de menor a mayor es:",n2,n1,n3)
if (n1<=n3<=n2):
    print("El orden de menor a mayor es:",n1,n3,n2)
if (n3<=n2<=n1):
    print("El orden de menor a mayor es:",n3,n2,n1)
if (n3<=n1<=n2):
    print("El orden de menor a mayor es:",n1,n3,n2)