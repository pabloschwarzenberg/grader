numero = int(input("Ingrese numero entero: "))
lista = []
while numero > 1:
    if numero%2 == 0:
        lista.append(2)
        numero = numero//2
        continue
    if numero%3 == 0:
        lista.append(3)
        numero = numero//3
        continue
    if numero%5 == 0:
        lista.append(5)
        numero = numero//5
        continue
    if numero%7 == 0:
        lista.append(7)
        numero = numero//7
        continue
    if numero%11 == 0:
        lista.append(11)
        numero = numero//11
        continue
    if numero%13 == 0:
        lista.append(13)
        numero = numero//13
        continue
    if numero%17 == 0:
        lista.append(17)
        numero = numero//17
        continue
    if numero%19 == 0:
        lista.append(19)
        numero = numero//19
        continue
for i in lista:
    print(i)