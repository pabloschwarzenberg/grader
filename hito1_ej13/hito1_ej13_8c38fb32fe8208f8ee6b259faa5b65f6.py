#Factores Primos
lista=[]
numero=int(input("ingrese un numero"))
i=2
while i<=numero:
  if numero%i==0:
    lista.append(i)
    numero=numero/i
  else:
    i=i+1
for i in lista:
  print(i)