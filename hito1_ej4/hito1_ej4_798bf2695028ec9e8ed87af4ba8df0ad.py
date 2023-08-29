#Conversión de Decimal a Binario
# Solicitamos el número decimal
num_decimal = int(input("Ingrese un número decimal: "))

# Convertimos el número decimal a binario
num_binario = bin(num_decimal).replace("0b", "")

# Imprimimos el resultado
print("resultado=" + num_binario)