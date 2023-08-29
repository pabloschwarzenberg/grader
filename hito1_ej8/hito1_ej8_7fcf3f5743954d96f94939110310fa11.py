#Descomponer un número
 #Descomponer un número
#Crear una lista
n = input("ingrese numero: ")
lista = []
x = 0
for letra in n:
    lista.append(letra)
    x = x + 1

if x == 1:
    print(lista[0] +"U")
if x == 2:
    print(lista[0] + "D","+", lista[1] +"U")
if x == 3:
    print(lista[0] + "C","+", lista[1] +"D","+",lista[2] + "U")
if x == 4:
    print(lista[0] + "M","+", lista[1] +"C","+",lista[2] + "D","+",lista[3] + "U")
     