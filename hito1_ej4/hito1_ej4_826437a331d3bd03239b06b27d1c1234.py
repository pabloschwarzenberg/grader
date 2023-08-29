#Conversión de Decimal a Binario
numero = int(input("Ingrese el numero que desea convertir en binario: "))
numeroFinal = []
if numero == 0:
    print("resultado=0")
else:
    while numero != 0:
        binario = numero % 2
        numero = numero // 2
        numeroFinal.append(str(binario))
    numeroFinal.reverse()
    print("resultado=", "".join(numeroFinal))