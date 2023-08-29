#Cálculo del dígito verificador de un rut
rut = (input("Ingrese su rut (Sin puntos, y no ingresar el codigo verificador):"))

#Multiplicación del RUT por digitos

if int(len(rut)) == 8:
    a = int(rut[0])
    b = int(rut[1])
    c = int(rut[2])
    d = int(rut[3])
    e = int(rut[4])
    f = int(rut[5])
    g = int(rut[6])
    h = int(rut[7])

    suma = a*3+b*2+c*7+d*6+e*5+f*4+g*3+h*2

    resto = suma%11
    codver = 11 - resto

    if 0 <= codver < 10:
        print("dv= ",codver)
        
    elif codver==10:
        codver = "k"
        print("dv= ",codver)

elif int(len(rut)) == 7:
    a = int(rut[0])
    b = int(rut[1])
    c = int(rut[2])
    d = int(rut[3])
    e = int(rut[4])
    f = int(rut[5])
    g = int(rut[6])

    suma = a*9+b*4+c*5+d*6+e*7+f*8+g*9

    resto = suma%11
    codver = resto

    if 0 <= codver < 10:
        print("dv= ",codver)
        
    elif codver==10:
        codver = "k"
        print("dv= ",codver)