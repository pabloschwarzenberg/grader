#Descomponer un número
numero = int(input('Ingrese un numero de hasta 4 cifras: '))

str_numero = str(numero)

#1230
if len(str_numero) == 4:
    m = str_numero[0]+'M'
    c = str_numero[1]+'C'
    d = str_numero[2]+'D'
    u = str_numero[3]+'U'
    print('{} + {} + {} + {}'.format(m, c, d, u))

elif len(str_numero) == 3:
    c = str_numero[0]+'C'
    d = str_numero[1]+'D'
    u = str_numero[2]+'U'
    print('{} + {} + {}'.format(c, d, u))

elif len(str_numero) == 2:
    d = str_numero[0]+'D'
    u = str_numero[1]+'U'
else:
    u = str_numero+'U'
    print(u)      