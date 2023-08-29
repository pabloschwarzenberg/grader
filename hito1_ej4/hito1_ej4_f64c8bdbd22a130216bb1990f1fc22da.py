#Conversión de Decimal a Binario
num = input("ingrese Nº: ")
n = int(num)
par = 2
numdiv = 0
aB = ""
aV = ""
aX = ""
aZ = ""
while n > 0:
    if n % 2 == 0:
        numdiv = n // par
        n = numdiv
        aB = str(aB) + str("0")
        aX = aB[0:1]
    else:
        numdiv = n // par
        aV = str(aV) + str("1")
        n = numdiv
        aX = aV[0:1]
    aZ = aX + aZ
print("resultado = ", aZ)