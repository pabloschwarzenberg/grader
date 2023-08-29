#Cálculo del dígito verificador de un rut
rut=(input("Inserte su rut: "))
if len(rut)==8:
    a = int(rut[7]) * 2
    b = int(rut[6]) * 3
    c = int(rut[5]) * 4
    d = int(rut[4]) * 5
    e = int(rut[3]) * 6
    f = int(rut[2]) * 7
    g = int(rut[1]) * 2
    h = int(rut[0]) * 3
    suma1 = a + b + c + d + e + f + g + h
    modulo1 = suma1 // 11
    print(suma1)
    print(modulo1)
    operacion = suma1 - (11 * modulo1)
    print(operacion)
    operacion1 = 11 - operacion
    if operacion1 == 11:
        print("dv=", 0)
    elif operacion1 == 10:
        print("dv=k")
    else:
        print("dv=", operacion1)
elif len(rut)==7:
    a = int(rut[6]) * 2
    b = int(rut[5]) * 3
    c = int(rut[4]) * 4
    d = int(rut[3]) * 5
    e = int(rut[2]) * 6
    f = int(rut[1]) * 7
    g = int(rut[0]) * 2
    suma1 = a + b + c + d + e + f + g 
    modulo1 = suma1 // 11
    print(suma1)
    print(modulo1)
    operacion = suma1 - (11 * modulo1)
    print(operacion)
    operacion1 = 11 - operacion
    if operacion1 == 11:
        print("dv=", 0)
    elif operacion1 == 10:
        print("dv=k")
    else:
        print("dv=", operacion1)



