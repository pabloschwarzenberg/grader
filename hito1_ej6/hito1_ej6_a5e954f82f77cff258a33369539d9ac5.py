#Ordenar tres números
i=1
lista=[]
while i<=3:
  num=eval(input())
  lista.append(num)
  i=i+1
lista.sort()
print(lista)