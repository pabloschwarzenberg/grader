#Conversión de Decimal a Binario
#Ni idea como hacer eso
x=int(input('Ingrese un numero: '))
y = 0
multiplicador = 1

while x != 0:
 y = y + x % 2 * multiplicador
 x //= 2
 multiplicador *= 10

print(y)