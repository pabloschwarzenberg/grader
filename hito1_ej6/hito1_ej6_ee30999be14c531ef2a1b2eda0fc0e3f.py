#Ordenar tres números
numero1=int(input())
numero2=int(input())
numero3=int(input())
lista=[numero1,numero2,numero3]
print(lista)
lista.sort()
print(lista)
indice=0
for numero in lista:
  if indice==0:
    print(numero,end="")
  else:
    print(",",numero,end="")
  indice+=1