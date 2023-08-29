#Factores Primos
n = int(input("Ingrese Número: "))

m=2

while m<=n:

  if n%m==0:

    print(m)

    n = n/m

  else:

    m+=1
