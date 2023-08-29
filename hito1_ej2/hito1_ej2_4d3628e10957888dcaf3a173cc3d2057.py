#Contestador de celular
numeroTelefono = int(input('Ingresa un numero telefonico de 8 cifras: '))
hora = int(input('Ingresa una hora del dia marcadas desde 0 a 23: '))

excepcion1 = numeroTelefono%1000
excepcion2 = numeroTelefono//100000

if hora >= 0 and hora <= 7:
    print('CONTESTAR')
if hora >= 8 and hora <= 14 and excepcion1 != 909:
    print('NO CONTESTAR')
if excepcion1 == 909:
    print('CONTESTAR')
if hora >= 15 and hora <= 16:
    print('NO CONTESTAR')
if hora >= 17 and hora <= 19 and excepcion2 != 877:
    print('CONTESTAR')
if excepcion2 == 877:
    print('NO CONTESTAR')
if hora == 19 or hora == 20 or hora == 21 or hora == 22 or hora == 23:
    print('NO CONTESTAR')     