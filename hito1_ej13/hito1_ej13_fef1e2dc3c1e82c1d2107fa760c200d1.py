#Factores Primos
primos=[]
def descomponer(n):  
  for i in range(2,n+1):
    while n%i==0:
      primos.append(i)
      n=n/i
  return primos
numero=int(input("Ingresa un numero:"))
numero=descomponer(numero)
for i in primos:
  print(i)
