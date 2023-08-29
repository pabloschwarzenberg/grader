#Factores Primos
lista=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,67,61,72,73,79,83,89,97]
x=int(input("ingrese un numero"))
b=0
for i in range(len(lista)):
  a=x%(lista[b])
  if a==0:
    print(lista[b])
  b+=1  