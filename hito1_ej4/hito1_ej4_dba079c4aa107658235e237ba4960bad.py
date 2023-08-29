#Conversión de Decimal a Binario
#Ingreso de datos
numdecimal = int(input("Ingrese un numero para transformarlo a binario: "))

#Transformar el dato ingresado a binario
def decabin(decimal):
    if decimal == 0:
        return "0"
    binario = []

    while decimal > 0:
        residuo = decimal % 2
        binario.append(str(residuo))
        decimal = decimal // 2

    resultado = "".join(binario[::-1])

    return resultado
resbinario = decabin(numdecimal)

#Imprimir resultado
print("resultado =", resbinario)