# Escribe un programa que le pida al usuario un número de hasta 4 dígitos y que te entregue la descomposición en Unidades, Decenas, Centenas y Miles

numero = int(input("Ingresa un número de hasta 4 dígitos: "))
while len(str(numero)) < 1 or len(str(numero)) > 4:
    numero = int(input("Ingresa un número de hasta 4 dígitos: "))

longitud = len(str(numero))
# letra = ""
if(longitud == 4):
    letra = "MCDU"
elif(longitud == 3):
    letra = "CDU"
elif(longitud == 2):
    letra = "DU"
else:
    letra = "U"

conteo = 0
mensaje = ""
for i in str(numero):
    mensaje += i + letra[conteo]
    if(longitud -1 > conteo ):
        mensaje += "+"
    conteo += 1

print(mensaje)