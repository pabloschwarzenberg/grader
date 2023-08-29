#Factores Primos
N = int(input("ingrese un número: "))
P=2
while P<=N:
  if N%P==0:
    print(P)
    N = N/P
  else:
    P+=1   