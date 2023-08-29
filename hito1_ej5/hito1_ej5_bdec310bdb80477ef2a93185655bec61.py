#Cálculo del dígito verificador de un rut
rut = str(input("Ingrese su rut sin dígito verificador, ni puntos: "))
if len(rut) == 8:
    rinv = rut[::-1]
    m1 = int(rinv[0])*2
    m2 = int(rinv[1])*3
    m3 = int(rinv[2])*4
    m4 = int(rinv[3])*5
    m5 = int(rinv[4])*6
    m6 = int(rinv[5])*7
    m7 = int(rinv[6])*2
    m8 = int(rinv[7])*3

    suma = m1+m2+m3+m4+m5+m6+m7+m8
    resto = suma%11
    divisor = 11 - resto

    if divisor == 10:
        print("dv =  K")
    elif divisor == 11:
        print("dv = 0")
    else:
        print("dv = ",divisor)

elif len(rut) == 7:
    rinv = rut[::-1]
    m1 = int(rinv[0])*2
    m2 = int(rinv[1])*3
    m3 = int(rinv[2])*4
    m4 = int(rinv[3])*5
    m5 = int(rinv[4])*6
    m6 = int(rinv[5])*7
    m7 = int(rinv[6])*2

    suma = m1+m2+m3+m4+m5+m6+m7
    resto = suma%11
    divisor = 11 - resto

    if divisor == 10:
        print("dv=K")
    elif divisor == 11:
        print("dv=0")
    else:
        print("dv=",divisor)      