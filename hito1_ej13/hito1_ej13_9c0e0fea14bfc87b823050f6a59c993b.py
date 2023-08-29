#Factores Primos
x = int(input("Ingresa un numero: "))

n=2
 
while n<=x:
  if x%n==0:
    print(n)
    x=x/n
  else:
      n+=1