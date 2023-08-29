#Contestador de celular
numero = str(input('Ingrese su número de celular: '))
hora = int(input('Ingrese la hora en que recibió la llamada: '))
#numero=str(numero)
a=numero[5:8]
e=numero[0:3]
b=str(909)
c=str(877)

if 7 <= hora <= 14:
    if b == a:
        print('CONTESTAR')
    else:
        print('NO CONTESTAR')
else:
    if 17 <= hora <= 19:
        if c == e:
            print('NO CONTESTAR')
        else:
            print("CONTESTA")

    else:
        print("NO CONTESTAR")