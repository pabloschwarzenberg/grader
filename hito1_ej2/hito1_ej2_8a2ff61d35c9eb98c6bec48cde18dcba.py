#Contestador de celular
nume = int(input('Ingrese el nro telefónico(8 cifras): '))
num = str(nume)
nro_tel =list(num)
hr = int(input('Ingrese hora de llamada(0-23): '))
if hr>=0 and hr<=7:
    print('CONTESTAR')
elif hr<14:
        if nro_tel[5]=='9' and nro_tel[6]=='0' and nro_tel[7]=='9':
            print('contestar')
        else:
            print('NO CONTESTAR')
elif hr<17:
    print('NO CONTESTAR')
elif hr>=17 and hr<=19:
    if nro_tel[0]=='8' and nro_tel[1]=='7' and nro_tel[2]=='7':
        print('NO CONTESTAR')
    else:
        print('CONTESTAR')
else:
    print('NO CONTESTAR')