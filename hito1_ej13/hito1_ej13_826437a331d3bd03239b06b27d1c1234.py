#Factores Primos
numero = int(input("Dame un numero: "))
if numero == 1:
    x = " 1"
else:
    x = str()
if numero < 0:
    numero = numero * -1
    #print(numero)
while numero > 1:
    if numero%2 == 0:
        x += ("2\n")
        z = 2
    elif numero%3 == 0:
        x += ("3\n")
        z = 3
    elif numero%5 == 0:
        x += ("5\n")
        z = 5
    else:
        x += str(numero) + "\n"
        break
    numero = int(numero/z)
    #print(x)
if numero == 0:
    print("No se puede, no seai pao")
else:
    print(x)      