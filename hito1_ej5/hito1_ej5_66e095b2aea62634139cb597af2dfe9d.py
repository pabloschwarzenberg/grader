#Cálculo del dígito verificador de un rut
print("Para calcular digito verificador: ")
print("Para calcular digito verificador: ")
rut = str(input("Ingrse su rut sin dígito verificador, ni puntos:"))
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

    suma = p1+p2+p3+p4+p5+p6+p7+p8
    resto = suma%11
    digver = 11-resto

    if digver==10:
        print("Su dígito verificador es:" ,'dv=K')
    elif digver==11:
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

    suma = p1+p2+p3+p4+p5+p6+p7
    resto = suma%11
    digver = 11-resto

    if digver==10:
        print("Su dígito verificador es:" ,'dv=k')
    elif digver==11:
        print("Su dígito verificador es:" ,'dv=0')
    else:
        print("Su dígito verificador es:",'dv=3')      