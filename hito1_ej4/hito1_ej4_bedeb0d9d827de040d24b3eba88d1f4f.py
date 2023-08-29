#Conversión de Decimal a Binario
numero = int(input('Introduce el número a convertir a binario: '))

binario = ""
# valida si la parte entera es diferente a dos
# Ejemplo: 33 // 2 = 16
while numero // 2 != 0:
    # Ejemplo: resto de 33 es 1 + binario (se suma en reversa)
    binario = str(numero % 2) + binario
    # Ejemplo: vuelve a dividir 33 // 2 que da 16 y 16 es la nueva variable
    numero = numero // 2
binarioFinal = str(numero) + binario
print("resultado = ",binarioFinal)

     