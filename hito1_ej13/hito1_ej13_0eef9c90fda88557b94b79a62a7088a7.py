#Factores Primos
numero = int(input("Dame un numero: "))
lista = []
lista2 = [2, 3, 5, 7, 11, 13]
for x in lista2:
    divicion = numero % x
    if x == 1:
        continue
    if divicion == 0:
        lista.append(x)
    

for i in lista:
    print(i)