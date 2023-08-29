#Ordenar tres números
i=1
lista=[]
while i < 4:
    numero=int(input("Ingresa un numero:"))
    i+=1
    lista.append(numero)

lista.sort()
print(lista)      