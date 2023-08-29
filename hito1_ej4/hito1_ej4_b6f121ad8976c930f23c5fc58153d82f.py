#Conversión de Decimal a Binario
def decimal_a_binario(numero):
    binario = bin(numero)[2:]  # Convierte el número a binario y elimina el prefijo "0b"
    return binario

if __name__ == "__main__":
    numero_decimal = int(input("Ingrese un número decimal: "))

    resultado_binario = decimal_a_binario(numero_decimal)

    print("Resultado =", resultado_binario)
      