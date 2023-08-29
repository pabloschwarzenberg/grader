#Ordenar tres números
      #Joaquin
N1=int(input("primer numero:"))
N2=int(input("segundo numero:"))
N3=int(input("tercer numero:"))
if(N1<=N2<=N3):
 print("El orden de menor a mayor es",N1,',',N2,',',N3)
if(N3<=N2<=N1):
    print("El orden de menor a mayor es",N3,',',N2,',',N1)
if(N2<=N3<=N1):
    print("El orden de menor a mayor es",N2,',',N3,',',N1)
if(N1<=N3<=N2):
    print("El orden de menor a mayor es",N1,',',N3,',',N2)
if(N2<=N1<=N3):
    print("El orden de menor a mayor es",N2,',',N1,',',N3)
if(N3<=N1<=N2):
    print("El orden de menor a mayor es",N3,',',N1,',',N2)      