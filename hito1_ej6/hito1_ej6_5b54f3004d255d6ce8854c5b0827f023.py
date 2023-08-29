#Ordenar tres números
#Ordenar tres números
n1=eval(input("Ingrese el primer numero: "))
n2=eval(input("Ingrese el segundo numero: "))
n3=eval(input("Ingrese el tercer numero: "))
if(n1<=n2<=n3):
    print("El orden de menor a mayor es",n1,',',n2,',',n3)
if(n3<=n2<=n1):
    print("El orden de menor a mayor es",n3,',',n2,',',n1)
if(n2<=n3<=n1):
    print("El orden de menor a mayor es",n2,',',n3,',',n1)
if(n1<=n3<=n2):
    print("El orden de menor a mayor es",n1,',',n3,',',n2)
if(n2<=n1<=n3):
    print("El orden de menor a mayor es",n2,',',n1,',',n3)
if(n3<=n1<=n2):
    print("El orden de menor a mayor es",n3,',',n1,',',n2)