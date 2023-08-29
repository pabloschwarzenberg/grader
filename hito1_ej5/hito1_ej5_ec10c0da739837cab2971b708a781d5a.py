#Cálculo del dígito verificador de un rut
rut = input("Dame tu rut:",)
rut_string = str(rut)
largo = len(rut_string)

if largo == 7:
    dos = int(rut[6]) * 2
    tres = int(rut[5]) * 3
    cuatro = int(rut[4]) * 4
    cinco = int(rut[3]) * 5
    seis = int(rut[2]) * 6
    siete = int(rut[1]) * 7
    dos_1 = int(rut[0]) * 2

    suma = dos+tres+cuatro+cinco+seis+siete+dos_1

    m11 = suma//11
    resto = suma - (11*m11)
    dv = 11 - resto
    if dv == 11:
        print("dv=0")
    elif dv == 10:
        print("dv=k")
    else:
        print("dv={}".format(dv))

elif largo == 8:
    dos = int(rut[7]) * 2
    tres = int(rut[6]) * 3
    cuatro = int(rut[5]) * 4
    cinco = int(rut[4]) * 5
    seis = int(rut[3]) * 6
    siete = int(rut[2]) * 7
    dos_1 = int(rut[1]) * 2
    tres_1 = int(rut[0]) * 3

    suma = dos+tres+cuatro+cinco+seis+siete+dos_1+tres_1

    m11 = suma//11
    resto = suma - (11*m11)
    dv = 11 - resto
    if dv == 11:
        print("dv=0")
    elif dv == 10:
        print("dv=k")
    else:
        print("dv={}".format(dv))