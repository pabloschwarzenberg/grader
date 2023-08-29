#ENTRADA
num= int(input("Ingrese un número: "))
binario=""

#CÁLCULO DE BINARIO
if (num > 0):
    while (num > 0):
        if (num % 2) == 0:
            binario = "0" + binario
        else:
            binario = "1" + binario
        num = int( num / 2)
    print("Resultado = " + str(binario))
else:
    print("Ingrese un número positivo")
