#Descomponer un número
numero = input("numero: ")
lista = []
a = 0
for letra in numero:
    lista.append(letra)
    a = a + 1

if a == 1:
    print(lista[0] +"U")
if a == 2:
    print(lista[0] + "D","+", lista[1] +"U")
if a == 3:
    print(lista[0] + "C","+", lista[1] +"D","+",lista[2] + "U")
if a == 4:
    print(lista[0] + "M","+", lista[1] +"C","+",lista[2] + "D","+",lista[3] + "U")