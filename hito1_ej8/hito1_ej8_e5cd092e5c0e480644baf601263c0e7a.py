#Descomponer un número
numero = int(input("Ingresa un numero de 4 digitos: "))
respaldo = numero

d1 = numero%10
numero = numero // 10

d2 = numero%10
numero = numero // 10

d3 = numero%10
numero = numero // 10


d4 = numero%10
numero = numero // 10


if 0 <= respaldo < 10:
    Digitosdescompuestos= str(d1)+ "U"

if 10 <= respaldo < 100:
    Digitosdescompuestos =  str(d2) + "D" + "+" + str(d1) + "U"
if 100 <= respaldo < 1000:
    Digitosdescompuestos =  str(d3) + "C" + "+" + str(d2) + "D" + "+" + str(d1) + "U"
if 1000 <= respaldo < 10000:
    Digitosdescompuestos =  str(d4) + "M" + "+" + str(d3) + "C" + "+" + str(d2) + "D" + "+" + str(d1) + "U"

print(Digitosdescompuestos)      