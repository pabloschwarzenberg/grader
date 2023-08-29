#Contestador de celular
Numero=int(input('ingrese el numero telefonico:'))
Hora=int(input('ingrese la hora de llamada:'))
if 10000000<=Numero<100000000 and 0<=Hora<=23:
    if 0<=Hora<=7:
        print('CONTESTAR')
    elif 7<Hora<14:
        if Numero%1000==909:
            print('CONTESTAR')
        else:
            print('NO CONTESTAR')
    elif 17<=Hora<=19:
        if Numero//100000==877:
            print('NO CONTESTAR')
        else:
            print('CONTESTAR')
    else:
        print('NO CONTESTAR')
else:
    print('la operacion no se puede realizar con los caracteres dados,')
    print('porfavor ingrese otros')
        