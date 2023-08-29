num_fono=int(input('ingrese el numero telefonico, este debe ser de 8 digitos: '))
hora_llamada=int(input('ingrese la hora del llamadoelformato es de 24 horas y debe ser entre 0 y 23): '))

if len(str(num_fono))==8 and hora_llamada>=0 and hora_llamada<=23:

    if hora_llamada>=0  and hora_llamada<=7:
        print('CONTESTAR')

    elif hora_llamada>7 and hora_llamada<14 and (num_fono%1000)==909:
        print('CONTESTAR')

    elif hora_llamada>7 and hora_llamada<14:
        print('NO CONTESTAR')
    
    elif hora_llamada>=17 and hora_llamada<=19 and (num_fono%1000)==877:
        print('NO CONTESTAR')

    elif hora_llamada>=17 and hora_llamada<=19:
        print('NO CONTESTAR')

    elif hora_llamada>19:
        print('NO CONTESTAR')
    
else:
    print('Los valores ingresados no son validos.')      