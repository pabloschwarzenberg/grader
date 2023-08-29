#Contestador de celular
cel = int(input())
a = str(cel)
hora = int(input())

if len(a) != 8:
    print('8 digitos')
elif hora >= 0 and hora <= 7 or hora >= 17 and hora <= 19 and cel//100000 != 877 or hora > 7 and hora < 14 and cel % 1000 == 909:
    print('CONTESTAR')
else:
    print('NO CONTESTAR')      