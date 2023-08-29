#Descomponer un número
numero = int(input('Ingrese su número: '))
numerostr = str(numero)

if len(str(numero)) == 1:
    print(numerostr[0] + 'U')
elif len(str(numero)) == 2:
    print((numerostr[0] + 'D'), '+', (numerostr[1] + 'U'))
elif len(str(numero)) == 3:
    print((numerostr[0] + 'C'), '+', (numerostr[1] + 'D'), '+', (numerostr[2] + 'U'))
elif len(str(numero)) == 4:
    print((numerostr[0] + 'M'), '+', (numerostr[1] + 'C'), '+', (numerostr[2] + 'D'), '+', (numerostr[3] + 'U'))
else:
    print('Error. Ingrese un número menor o igual que 4')