#Factores Primos
n=int(input("Ingrese Numero: "))
i=2
while n!=1:
  if n %i==0:
    print(i)
    n=n/i
  else:
    i=i+1      