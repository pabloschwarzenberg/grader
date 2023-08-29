#Ordenar tres números
lista=[]
contador=0
while contador<3:
    lista.append(int(input('ingrese  un numero: ')))
    contador+=1

lista.sort()

print(lista)
