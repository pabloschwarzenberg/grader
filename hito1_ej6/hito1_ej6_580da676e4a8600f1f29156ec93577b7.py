#Ordenar tres números
primo=1
lista=[]
while primo <= 3:
  numero=eval(input())
  lista.append(numero)
  primo = primo + 1
lista.sort()
print(lista)