rut = str(input("Ingrese rut :"))
intento_l = list(rut)

resultado = len(intento_l)

if (resultado ==7):
    n1 = int(intento_l[0]*1)*2
    n2 = int(intento_l[1]*1)*7
    n3 = int(intento_l[2]*1)*6
    n4 = int(intento_l[3]*1)*5
    n5 = int(intento_l[4]*1)*4
    n6 = int(intento_l[5]*1)*3
    n7 = int(intento_l[6]*1)*2
    suma = (n1+n2+n3+n4+n5+n6+n7)
    modulo = (suma//11)
    resto = suma-(11*modulo)
    resultadof = (11-resto)
    
    if (resultadof == 11):
        print("dv=0")
    elif(resultadof == 10):
        print("dv=K")
    else:
        print("dv=", resultadof)
elif (resultado == 8):
    n1 = int(intento_l[0]*1)*3
    n2 = int(intento_l[1]*1)*2
    n3 = int(intento_l[2]*1)*7
    n4 = int(intento_l[3]*1)*6
    n5 = int(intento_l[4]*1)*5
    n6 = int(intento_l[5]*1)*4
    n7 = int(intento_l[6]*1)*3
    n8 = int(intento_l[7]*1)*2

    suma = (n1+n2+n3+n4+n5+n6+n7+n8)
    modulo = (suma//11)
    resto = suma-(11*modulo)
    resultadof = (11-resto)
    if (resultadof == 11):
        print("dv=0")
    elif(resultadof == 10):
        print("dv=K")
    else:
        print("dv=", resultadof)
