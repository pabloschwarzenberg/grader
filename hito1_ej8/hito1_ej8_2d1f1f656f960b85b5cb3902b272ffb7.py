#Descomponer un número
X=int(input("ingrese su numero de 4 numeros como maximo:"))
M=X//1000
C=(X%1000)//100
D=((X%1000)%100)//10
U=((X%1000)%100)%10
if 0<X<10000:
  print(str(M)+"M + "+str(C)+"C + "+str(D)+"D + "+str(U)+"U")
else:
  print("Debe ser un numero natural de maximo 4 cifras")