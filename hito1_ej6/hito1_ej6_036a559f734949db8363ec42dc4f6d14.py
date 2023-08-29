#Ordenar tres números
lista=[]
largo=3
for i in range(largo):
  lista.append(0)
  
for i in range(largo):
  lista[i]=int(input("Ingrese Numero {i+1}: "))
lista.sort()
print(lista)  