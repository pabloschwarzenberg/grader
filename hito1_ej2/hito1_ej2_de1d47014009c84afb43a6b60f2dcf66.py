#Contestador de celular
T = eval(input('Ingrese número telefonico:'))
H = eval(input('Ingrese hora de llamada:'))

rt = T
rh = H

r =T%1000
   
x =T//100000

if (10000000 <= rt <= 99999999) and (0 <= rh <= 23):
    if 0 <= rh <= 7:
        print('CONTESTAR')
    if 8 <= rh <= 14:
        if r == 909:
            print('CONTESTAR')
        else:
            print('NO CONTESTAR')
    if 15 <= rh <= 16:
        print('NO CONTESTAR')
    if 17 <= rh <= 19:
        if x == 877:
            print('NO CONTESTAR')
        else:
            print('CONTESTAR')
    if 20 <= rh <= 23:
        print('NO CONTESTAR')
else:
    print('Error: teléfono u hora de llamada inválidos.')      