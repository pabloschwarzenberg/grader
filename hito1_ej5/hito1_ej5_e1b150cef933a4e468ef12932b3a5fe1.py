rut = str(input("Ingrese su rut sin dígito verificador, ni puntos:"))
if len(rut)==8:
    rinv = rut[::-1]
    p1=int(rinv[0])*2
    p2=int(rinv[1])*3
    p3=int(rinv[2])*4
    p4=int(rinv[3])*5
    p5=int(rinv[4])*6
    p6=int(rinv[5])*7
    p7=int(rinv[6])*2
    p8=int(rinv[7])*3

    a = p1+p2+p3+p4+p5+p6+p7+p8
    b = a%11
    digito_verificador = 11-b

    if digito_verificador==10:
        print("Su dígito verificador es:" ,'dv=K')
    elif digito_verificador==11:
        print("Su dígito verificador es:" ,'dv=0')
    else:
        print("Su dígito verificador es:",'dv=3')

elif len(rut)==7:
    rinv = rut[::-1]
    p1=int(rinv[0])*2
    p2=int(rinv[1])*3
    p3=int(rinv[2])*4
    p4=int(rinv[3])*5
    p5=int(rinv[4])*6
    p6=int(rinv[5])*7
    p7=int(rinv[6])*2

    a = p1+p2+p3+p4+p5+p6+p7
    b = a%11
    digito_verificador = 11-b

    if digito_verificador==10:
        print("Su dígito verificador es:" ,'dv=k')
    elif digito_verificador==11:
        print("Su dígito verificador es:" ,'dv=0')
    else:
        print("Su dígito verificador es:",'dv=3')