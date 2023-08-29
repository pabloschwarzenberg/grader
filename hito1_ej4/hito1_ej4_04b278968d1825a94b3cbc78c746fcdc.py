# Entrada
n = int(input("ingresa un número:"))
resultado = ""
# Procesamiento
while n > 0:
    resultado = (str(n % 2)) + resultado
    n //= 2
#Salida
print("resultado= ",(resultado))

