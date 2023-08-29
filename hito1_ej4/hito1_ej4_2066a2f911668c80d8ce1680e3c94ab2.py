n = int(input("Ingrese número: "))
resultado = ""

while n != 0:
    binario = n % 2
    cociente = n // 2
    resultado = str(binario) + resultado
    n = cociente

print(f"resultado={resultado}")   