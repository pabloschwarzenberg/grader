#Conversión de Decimal a Binario
d = int(input("Ingresa un número decimal: "))
b =""
while d > 0:
 r = int(d % 2)
 d = int(d / 2)
 b = str(r) + b

print( "Resultado=",(b) )
