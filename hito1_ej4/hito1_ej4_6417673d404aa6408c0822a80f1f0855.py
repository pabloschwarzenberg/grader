decimal = int(input("Ingresa un número decimal: "))

# Verificar si el número es negativo
negative = False
if decimal < 0:
    negative = True
    decimal = abs(decimal)

# Convertir decimal a binario
binary = ""
while decimal > 0:
    remainder = decimal % 2
    binary = str(remainder) + binary
    decimal = decimal // 2

# Agregar el signo "-" si el número es negativo
if negative:
    binary = "-" + binary

print("resultado=", binary)
