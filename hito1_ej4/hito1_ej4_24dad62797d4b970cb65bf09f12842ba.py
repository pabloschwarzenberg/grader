#Conversión de Decimal a Binario
numero = int(input("Ingrese el numero que desea convertir en binario"))
resultado = ""
while numero // 2 != 0:
    resultado = str(numero % 2) + resultado
    numero = numero // 2
print ("resultado =", (str(numero)+resultado))
