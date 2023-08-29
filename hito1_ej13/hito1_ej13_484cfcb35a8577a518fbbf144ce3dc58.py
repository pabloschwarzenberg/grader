#Factores Primos
numero = int(input("Ingrese un Número: "))

n=2

while n<=numero:

  if numero%n==0:

    print(n)

    numero = numero/n

  else:

    n+=1     