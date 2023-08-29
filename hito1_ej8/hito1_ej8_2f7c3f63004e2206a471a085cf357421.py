#Descomponer un número
numero = int(input("Ingrese un numero de hasta 4 digitos: "))

if len(str(numero)) == 4:
    miles = str(numero//1000)
    numero %= 10**3
    centenas = str(numero//100)
    numero %= 10**2
    decenas = str(numero//10)
    numero %= 10
    unidades = str(numero)

    print(miles+"M",centenas+"C",decenas+"D",unidades+"U", sep ="+")

if len(str(numero)) == 3:
    centenas = str(numero//100)
    numero %= 10**2
    decenas = str(numero//10)
    numero %= 10
    unidades = str(numero)

    print(centenas+"C",decenas+"D",unidades+"U", sep ="+")

if len(str(numero)) == 2:
    decenas = str(numero//10)
    numero %= 10
    unidades = str(numero)

    print(decenas+"D",unidades+"U", sep ="+")

if len(str(numero)) == 1:
    unidades = str(numero)

    print(unidades+"U")      