numero = int(input("Ingrese un número de hasta 4 dígitos: "))

unidades = numero % 10
decenas = (numero // 10) % 10
centenas = (numero // 100) % 10
miles = (numero // 1000) % 10

resultado = ""

if miles != 0:
    resultado += str(miles) + "M + "
if centenas != 0:
    resultado += str(centenas) + "C + "
if decenas != 0:
    resultado += str(decenas) + "D + "
resultado += str(unidades) + "U"

print("Descomposición:", resultado)