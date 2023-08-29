# Obtener el número decimal de entrada
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario utilizando la función bin()
numero_binario = bin(numero_decimal)

# Imprimir el resultado
print("Resultado =", numero_binario[2:])
      