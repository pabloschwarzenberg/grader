#Cálculo del dígito verificador de un rut
rut = input('Ingrese su rut sin puntos ni dígito verificador: ')
rutstr = str(rut)
if len(str(rut)) == 8:
    uno = rutstr[7]
    dos = rutstr[6]
    tres = rutstr[5]
    cuatro = rutstr[4]
    cinco = rutstr[3]
    seis = rutstr[2]
    siete = rutstr[1]
    ocho = rutstr[0]
    result_1 = int(uno)*2
    result_2 = int(dos)*3
    result_3 = int(tres)*4
    result_4 = int(cuatro)*5
    result_5 = int(cinco)*6
    result_6 = int(seis)*7
    result_7 = int(siete)*2
    result_8 = int(ocho)*3
    suma =result_1 + result_2 + result_3 + result_4 + result_5 + result_6 + result_7 + result_8
    division = int(suma / 11)
    operatoria = suma - (int(division)*11)
    respuesta = 11 - operatoria
    if respuesta == 11:
        print('dv=', 0)
    elif respuesta == 10:
        print('dv=k')
    else:
        print('dv=', respuesta)

if  len(str(rut)) == 7:
    uno = rutstr[6]
    dos = rutstr[5]
    tres = rutstr[4]
    cuatro = rutstr[3]
    cinco = rutstr[2]
    seis = rutstr[1]
    siete = rutstr[0]
    result_1 = int(uno)*2
    result_2 = int(dos)*3
    result_3 = int(tres)*4
    result_4 = int(cuatro)*5
    result_5 = int(cinco)*6
    result_6 = int(seis)*7
    result_7 = int(siete)*2
    suma = result_1 + result_2 + result_3 + result_4 + result_5 + result_6 + result_7
    division = int(suma / 11)
    operatoria = suma - (int(division)*11)
    respuesta = 11 - operatoria
    if respuesta == 11:
        print('dv=', 0)
    elif respuesta == 10:
        print('dv= k')
    else:
        print('dv=', respuesta)