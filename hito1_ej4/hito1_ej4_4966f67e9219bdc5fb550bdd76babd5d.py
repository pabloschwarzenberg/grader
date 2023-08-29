decimal=int(input("Ingrese el numero a convertir: "))

binario=" "
while decimal > 0:
    residuo = decimal%2
    decimal = decimal//2
    binario = str(residuo) + binario
print("Resultado=", binario)

