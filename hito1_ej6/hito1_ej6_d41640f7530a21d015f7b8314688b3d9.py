#Ordenar tres números
lista =[]
veces = 0

while(veces<3):
    enteros = int(input("ingrese un numero entero: "))
    veces += 1
    lista.append(enteros)
    
lista.sort()
for numero in range(len(lista)):
    if numero != 0:
        print(", ", end="")
    print(lista[numero], end="")
      