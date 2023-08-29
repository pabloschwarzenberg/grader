def decimal_a_binario(decimal):
    binario = bin(decimal)[2:]  # Utilizamos la función bin() para convertir a binario y eliminamos el prefijo '0b'
    return binario

numero_decimal = int(input("Ingrese un número decimal: "))
numero_binario = decimal_a_binario(numero_decimal)

print(f"resultado= {numero_binario}")