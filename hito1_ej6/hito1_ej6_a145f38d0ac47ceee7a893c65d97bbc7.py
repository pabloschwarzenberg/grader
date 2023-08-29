#Ordenar tres números
n1=int(input("Ingrese número entero 1 ",))
n2=int(input("Ingrese número entero 2 ",))
n3=int(input("Ingrese número entero 3 ",))
if(n1<=n2<=n3):
    print("El orden de menor a mayor es",n1,',',n2,',',n3)
if(n3<=n2<=n1):
    print("El orden de menor a mayor es",n3,',',n2,',',n1)
if(n1<=n3<=n2):
    print("El orden de menor a mayor es",n1,',',n3,',',n2)
if(n2<=n3<=n1):
    print("El orden de menor a mayor es",n2,',',n3,',',n1)
if(n2<=n1<=n3):
    print("El orden de menor a mayor es",n2,',',n1,',',n3)
if(n3<=n1<=n2):
    print("El orden de menor a mayor es",n3,',',n1,',',n2)