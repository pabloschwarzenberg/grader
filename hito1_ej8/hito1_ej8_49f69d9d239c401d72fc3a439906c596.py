#Descomponer un número
numero = int(input('Ingrese un numero: '))

while numero > 9999:
    numero = int(input('Ingrese un numero: '))

if numero > 999:
    mil = numero // 1000
    centena = numero % 1000 // 100
    decena = numero % 1000 % 100 // 10
    unidad = numero % 1000 % 100 % 10
    print('%iM + %iC + %iD + %iU' % (mil, centena, decena, unidad))

elif numero > 99:
    centena = numero // 100
    decena = numero % 100 // 10
    unidad = numero % 100 % 10
    print('%iC + %iD + %iU' % (centena, decena, unidad))

elif numero > 9:
    decena = numero // 10
    unidad = numero % 10
    print('%iD + %iU' % (decena, unidad))

else:
    print('%iU' % numero)