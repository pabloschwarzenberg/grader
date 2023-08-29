#Conversión de Decimal a Binario
numdec = int(input("Ingrese un numero decimal: "))

if numdec == 0:
    numbin = 0

else:
    numbin = ""

    while numdec > 0:
        residuo = numdec % 2
        numbin = str(residuo) + numbin
        numdec = numdec // 2

print("Resultado =", numbin)