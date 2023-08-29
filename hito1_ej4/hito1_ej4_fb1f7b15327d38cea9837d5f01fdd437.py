from os import system
system("cls")

def decimal_a_binario(decimal):
    return bin(decimal)[2:]

numero_decimal = int(input("Ingrese un número decimal: "))
resultado = decimal_a_binario(numero_decimal)
print("resultado =", resultado)      