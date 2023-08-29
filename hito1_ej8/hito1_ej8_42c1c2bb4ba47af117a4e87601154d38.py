#Descomponer un número
nu = float(input("Introdusca un numero: "))
n= str(nu)
print('Numero completo: '.format(nu))

if nu >999 and nu < 10000:
    print('{}M+{}C+{}D+{}U'.format(n[0], n[1], n[2], n[3]))
if nu > 99 and nu < 1000:
    print('{}C+{}D+{}U'.format(n[0], n[1], n[2]))
if nu > 9 and nu < 100:
    print('{}D+{}U'.format(n[0], n[1]))
if nu>= 0 and nu< 10:
    print('{}U'.format(n[0]))      