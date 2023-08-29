numero_decimal = int(input("Ingrese un número decimal: "))

# Verificar si el número es negativo
es_negativo = False
if numero_decimal < 0:
    es_negativo = True
    numero_decimal = abs(numero_decimal)

# Inicializar la lista para almacenar los dígitos binarios
binario = []

# Caso especial para el número 0
if numero_decimal == 0:
    binario.append(0)

# Convertir el número decimal a binario
while numero_decimal > 0:
    residuo = numero_decimal % 2
    binario.append(residuo)
    numero_decimal = numero_decimal // 2

# Invertir la lista de dígitos binarios
binario.reverse()

# Agregar el signo negativo si corresponde
if es_negativo:
    binario.insert(0, "-")

# Convertir la lista de dígitos binarios a una cadena de texto
binario_str = "".join(str(digito) for digito in binario)

# Imprimir el resultado
print("Resultado =", binario_str)