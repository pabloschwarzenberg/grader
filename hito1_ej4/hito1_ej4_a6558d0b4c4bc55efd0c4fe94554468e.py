# Entrada
x = float(input("Ingrese numero: "))
# Procesamiento
número = int(x)
número_binario = bin(número)
número_decimal = (int(número_binario[2:]))
# Salida
print("resultado =", número_decimal)
