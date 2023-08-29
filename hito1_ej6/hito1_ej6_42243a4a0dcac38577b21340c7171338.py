#Ordenar tres números
N1=int(input("ingrese un numero: "))
N2=int(input("ingrese un numero: "))
N3=int(input("ingrese un numero: "))
if N1 < N2 < N3 and N1 = N2 = N3 and N1 < N2 =N3 and N1 = N2 < N3:
  print(N1,N2,N3)
if N3 < N2 < N1 and N3 = N2 < N1 and N3 < N2 = N1:
  print(N3,N2,N1)
if N2 < N3 < N1 and N2 = N3 < N1 and N2 < N3 = N1:
    print(N2,N3,N1)
if N1 < N3 < N2 and N1 < N3 = N2 and N1 = N3 < N2: 
  print(N1,N3,N2)

  