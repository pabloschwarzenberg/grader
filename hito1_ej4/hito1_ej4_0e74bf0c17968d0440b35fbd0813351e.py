#Conversión de Decimal a Binario

#Ingreso de datos

nd = int(input("Ingresa un número decimal: "))

#Operacion

negativo = False
if nd < 0:
    negativo = True
    nd = -nd

binario = 0
contador = 0
while nd > 0:
    res = nd % 2
    binario += res * (10 ** contador)
    nd //= 2
    contador += 1

if negativo:
    binario = -binario

#Resultado
print("Resultado =", binario)

