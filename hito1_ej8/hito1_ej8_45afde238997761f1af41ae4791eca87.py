numero = int(input("Ingrese un número de hasta 4 dígitos: "))

miles = numero // 1000
centenas = (numero // 100) % 10
decenas = (numero // 10) % 10
unidades = numero % 10

resultado = ""

if miles > 0:
    resultado += str(miles) + "M + "
if centenas > 0:
    resultado += str(centenas) + "C + "
if decenas > 0:
    resultado += str(decenas) + "D + "
if unidades > 0:
    resultado += str(unidades) + "U"

print(resultado)

      