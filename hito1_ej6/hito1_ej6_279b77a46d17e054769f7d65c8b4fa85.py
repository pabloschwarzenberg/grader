#Ordenar tres números
lista = []
cont = 1
numeros = 0
for elements in range (3):
    n = int(input("ingrese numero {cont}: "))
    lista.append(n)
    cont +=1
lista.sort()
for elementos in lista:
    print(elementos,end="")
    numeros += 1
    if numeros != 3:
        print(",",end="")
print(" ")