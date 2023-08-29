#Conversión de Decimal a Binario
numBin = ""
numDec = float(input("Ingrese un numero: "))

result = numDec 

while result > 0:
    resto = result % 2
    result = result // 2
    numBin = str(int(resto)) + numBin

print("Resultado=", numBin)