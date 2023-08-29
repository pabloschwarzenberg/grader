#Factores Primos
z = int(input("Ingrese Número: "))

n=2

while n<=z:

  if z%n==0:

    print(n)

    z  = z/n

  else:

    n+=1
    