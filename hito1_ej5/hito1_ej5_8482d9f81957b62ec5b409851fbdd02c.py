#Cálculo del dígito verificador de un rut

rut = input("ingrese su rut, sin el numero después del guión: ")
if len(rut) == 8:
    se = (int(rut[7]))*2
    s = (int(rut[6]))*3
    q = (int(rut[5]))*4
    c = (int(rut[4]))*5
    t = (int(rut[3]))*6
    seg = (int(rut[2]))*7
    p = (int(rut[1]))*2
    n = (int(rut[0]))*3

    total = se + s + q + c + t + seg + p + n
    
    parte_entera = (total // 11)

    resta_parte_entera = total - (parte_entera * 11)

    

    digitoverificador = 11 - resta_parte_entera

    

    if ( digitoverificador == 11):
        print("dv=0")
    elif ( digitoverificador == 10):
        print("dv=k")

    else:
        print("dv =", digitoverificador)

elif len(rut) == 7:
    s = (int(rut[6]))*2
    q = (int(rut[5]))*3
    c = (int(rut[4]))*4
    t = (int(rut[3]))*5
    seg= (int(rut[2]))*6
    p = (int(rut[1]))*7
    n= (int(rut[0]))*2

    total = s + q + c + t + seg + p + n
    
    parte_entera = ((total // 11))

    resta_parte_entera = total - (parte_entera * 11)

    

    digitoverificador = 11 - resta_parte_entera

    

    if ( digitoverificador == 11):
        print("dv=0")
    elif ( digitoverificador == 10):
        print("dv=k")

    else:
        print("dv =", digitoverificador)

