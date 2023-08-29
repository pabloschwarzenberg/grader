#Conversión de Decimal a Binario
def conversor(numero):
    resultado = ""
    while(numero//2 != 0):
        numerito = numero%2
        resultado += str(numerito)
        numero = numero // 2
        if(numero//2 == 0):
            numerito = numero%2
            resultado += str(numerito)
            numero = numero // 2
    return resultado[::-1]

numero = int(input("Ingrese un numero decimal: "))
resultado = conversor(numero)
print("resultado =",resultado)