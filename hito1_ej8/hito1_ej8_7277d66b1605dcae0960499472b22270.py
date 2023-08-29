#Descomponer un número
def descomposicion(num):
    descomposicion_str = ""

    if num >= 1000:
        miles = num // 1000
        descomposicion_str += str(miles) + "M + "
        num %= 1000

    if num >= 100:
        centenas = num // 100
        descomposicion_str += str(centenas) + "C + "
        num %= 100

    if num >= 10:
        decenas = num // 10
        descomposicion_str += str(decenas) + "D + "
        num %= 10

    descomposicion_str += str(num) + "U"

    return descomposicion_str

# Ejemplo de uso
numero = int(input("Ingresa un número de hasta 4 dígitos: "))
resultado = descomposicion(numero)
print("Descomposición:", resultado)