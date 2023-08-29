# Escribe un programa que reciba como entrada un número decimal e imprima el resultado de convertirlo a binario.
# Por ejemplo, al ingresar el número 33 tu programa debiera imprimir el siguiente mensaje:

# resultado=100001


# Conversión de Decimal a Binario
def decimal_a_binario(decimal):
    binario = bin(decimal)[2:]
    return binario


numero_decimal = int(input("Ingrese un número decimal: "))
numero_binario = decimal_a_binario(numero_decimal)
print("Resultado =", numero_binario)
