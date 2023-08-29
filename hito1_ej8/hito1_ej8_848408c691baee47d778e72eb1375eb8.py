#Descomponer un número
Numero = int(input("Ingrese un número de hasta 4 digitos:"))

NumeroString = str(Numero)

if len(str(Numero)) == 1:

    print(NumeroString[0] + "U")
elif len(str(Numero)) == 2:

    print(NumeroString[0] + "D + " + NumeroString[1] + "U")
elif len(str(Numero)) == 3:

    print(NumeroString[0] + "C + " + NumeroString[1] + "D + " + NumeroString[2] + "U")
elif len(str(Numero)) == 4:

    print(NumeroString[0] + "M + " + NumeroString[1] + "C + " + NumeroString[2] + "D + " + NumeroString[3] + "U")      