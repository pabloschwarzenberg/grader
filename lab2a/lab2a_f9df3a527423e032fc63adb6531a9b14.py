#múltiplos
N1=int(input("ingrese numero de inicio"))
N2=int(input("ingrese numero final"))

while N1<=N2:

  N1=N1+1
  if N1%2==0 and N1%7==0:
         print(N1)