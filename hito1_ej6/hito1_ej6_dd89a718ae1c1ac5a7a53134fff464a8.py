#Ordenar tres números
n1=int(input("Ingrese el primer numero:"))
n2=int(input("Ingrese el segundo numero:"))
n3=int(input("Ingrese el tercer numero:"))
if(n1<=n2<=n3):
    print("El orden de menor a mayor es {}, {}, {}".format(n1, n2, n3))
if(n3<=n2<=n1):
    print("El orden de menor a mayor es {}, {}, {}".format(n3, n2, n1))
if(n2<=n3<=n1):
    print("El orden de menor a mayor es {}, {}, {}".format(n2, n3, n1))
if(n1<=n3<=n2):
    print("El orden de menor a mayor es {}, {}, {}".format(n1, n3, n2))
if(n2<=n1<=n3):
    print("El orden de menor a mayor es {}, {}, {}".format(n2, n1, n3))
if(n3<=n1<=n2):
    print("El orden de menor a mayor es {}, {}, {}".format(n3, n1 ,n2))