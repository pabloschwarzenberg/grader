contador=1
numeros=[]
for i in range(3):
  n=int(input("Ingrese numero : "))
  numeros.append(n)
  numeros.sort()
  contador=contador+1
print(numeros)