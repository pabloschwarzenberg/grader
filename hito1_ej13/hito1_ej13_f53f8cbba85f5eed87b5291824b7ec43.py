#Factores Primos
a=int(input("Ingrese numero: "))
primos=[]
for i in range(2,a+1):
  while a % i==0:
    primos.append(i)
    a=a/i

for i in primos:
  print(i)