#Contestador de celular
print('Ingrese el numero de 8 digitos y la hora en formato de 0 a 23hrs: ')
numero=int(input('Ingrese el numero de celular: '))
hora=int(input('Ingrese la hora del llamado: '))
ultimo=numero%1000
primero=numero//100000
if ultimo==909:
    print('CONTESTAR')
if primero==877:
    print('NO CONTESTAR')
if 0<=hora<=7:
    print('CONTESTAR')
if 7<hora<=14 and ultimo!=909:
    print('NO CONTESTAR')
if 17<=hora<=19 and primero!=877:
    print('CONTESTAR')
if hora>19:
    print('NO CONTESTAR')