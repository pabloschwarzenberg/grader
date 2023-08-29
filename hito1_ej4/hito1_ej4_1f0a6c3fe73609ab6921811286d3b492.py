decimal = float(input("ingresa el n"))
entero = int(decimal)

# Obtener la parte decimal del número decimal
parte_decimal = decimal - entero

# Convertir la parte entera a binario
binario_entero = ""
while entero > 0:
    binario_entero = str(entero % 2) + binario_entero
    entero = entero // 2

binario_decimal = ""
while parte_decimal > 0:
    parte_decimal *= 2
    bit = int(parte_decimal)
    binario_decimal += str(bit)
    parte_decimal -= bit
binario = binario_entero + "." + binario_decimal
print("resultado=",decimal)
print("resultado=",binario)