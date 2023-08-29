#Cálculo del dígito verificador de un rut
rut = input("Ingrese numero de rut(sin digito verificador:)")
rutstring = str(rut)
if len(str(rut)) == 8:
    uno = rutstring[7]
    dos = rutstring[6]
    tres = rutstring[5]
    cuatro = rutstring[4]
    cinco = rutstring[3]
    seis = rutstring[2]
    siete = rutstring[1]
    ocho = rutstring[0]
    resultado1 = int(uno)*2
    resultado2 = int(dos)*3
    resultado3 = int(tres)*4
    resultado4 = int(cuatro)*5
    resultado5 = int(cinco)*6
    resultado6 = int(seis)*7
    resultado7 = int(siete)*2
    resultado8 = int(ocho)*3
    suma = resultado1+resultado2+resultado3+resultado4+resultado5+resultado6+resultado7+resultado8
    entero = int(suma/11)
    final = suma - (int(entero)*11)
    respuesta = 11-final
    if respuesta == 11:
        print("dv=",0)
    elif respuesta == 10:
        print("dv=K")
    else:
        print("dv=",w)

elif len(str(rut)) == 7:
    uno = rutstring[6]
    dos = rutstring[5]
    tres = rutstring[4]
    cuatro = rutstring[3]
    cinco = rutstring[2]
    seis = rutstring[1]
    siete = rutstring[0]
    resultado1 = int(uno)*2
    resultado2 = int(dos)*3
    resultado3 = int(tres)*4
    resultado4 = int(cuatro)*5
    resultado5 = int(cinco)*6
    resultado6 = int(seis)*7
    resultado7 = int(siete)*2
    suma = resultado1 + resultado2 + resultado3 + resultado4 + resultado5 + resultado6 + resultado7
    entero = int(suma / 11)
    final = suma - (int(entero) * 11)
    respuesta = 11 - final
    if respuesta == 11:
        print("dv=",0)
    elif respuesta == 10:
        print("dv=K")
    else:
        print("dv=",respuesta)      