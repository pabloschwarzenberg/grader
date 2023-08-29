#Descomponer un número
num = int(input("Introduzca un numero: "))
n = str(num)
print('Numero completo: '.format(num))

if num > 999 and num < 10000:
    print('{}M+{}C+{}D+{}U'.format(n[0], n[1], n[2], n[3]))
if num > 99 and num < 1000:
    print('{}C+{}D+{}U'.format(n[0], n[1], n[2]))
if num > 9 and num < 100:
    print('{}D+{}U'.format(n[0], n[1]))
if num >= 0 and num < 10:
    print('{}U'.format(n[0]))