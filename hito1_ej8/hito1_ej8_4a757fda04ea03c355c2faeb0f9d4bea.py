#Descomponer un número
numero = int(input("Introduzca un numero: "))
n = str(numero)
print('Numero completo: '.format(numero))

if numero > 999 and numero < 10000:
    print('{}M+{}C+{}D+{}U'.format(n[0], n[1], n[2], n[3]))
if numero > 99 and numero < 1000:
    print('{}C+{}D+{}U'.format(n[0], n[1], n[2]))
if numero > 9 and numero < 100:
    print('{}D+{}U'.format(n[0], n[1]))
if numero >= 0 and numero < 10:
    print('{}U'.format(n[0]))
    