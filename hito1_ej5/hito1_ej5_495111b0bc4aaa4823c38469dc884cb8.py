#Cálculo del dígito verificador de un rut
rutnumero = int(input("Ingrese un rut, sin puntos, y sin el digito verificador: "))
rut = str(rutnumero)
if len(rut) == 7:
    num2 = int(rut[0]) * 2
    num3 = int(rut[1]) * 7
    num4 = int(rut[2]) * 6
    num5 = int(rut[3]) * 5
    num6 = int(rut[4]) * 4
    num7 = int(rut[5]) * 3
    num8 = int(rut[6]) * 2
    resultadofinal = 11 - ((num2 + num3 + num4 + num5 + num6 + num7 + num8) % 11)
    if resultadofinal == 11:
        print("dv=0")
    elif resultadofinal == 10:
        print("dv=K")
    else:
        print("dv=", resultadofinal)
if len(rut) == 8:
    num1 = int(rut[0]) * 3
    num2 = int(rut[1]) * 2
    num3 = int(rut[2]) * 7
    num4 = int(rut[3]) * 6
    num5 = int(rut[4]) * 5
    num6 = int(rut[5]) * 4
    num7 = int(rut[6]) * 3
    num8 = int(rut[7]) * 2
    resultadofinal = 11 - ((num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8) % 11)
    if resultadofinal == 11:
        print("dv=0")
    elif resultadofinal == 10:
        print("dv=K")
    else:
        print("dv=", resultadofinal)