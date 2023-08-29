# Solicitar el número decimal al usuario
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
def decimal_a_binario(numero):
    if numero == 0:
        return '0'
    
    bits = []
    while numero > 0:
        residuo = numero % 2
        bits.append(str(residuo))
        numero //= 2
    
    bits.reverse()
    binario = ''.join(bits)
    return binario

numero_binario = decimal_a_binario(numero_decimal)

# Mostrar el numero convertido
print("El número binario es:", numero_binario)
      