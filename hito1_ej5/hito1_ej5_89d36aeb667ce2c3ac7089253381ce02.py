#Cálculo del dígito verificador de un rut
print("Para calcular digito verificador")
rut = str(input("Ingrse su rut sin dígito verificador ni puntos:"))
if len(rut)==8:
    rinv = rut[::-1]
    s1=int(rinv[0])*2
    s2=int(rinv[1])*3
    s3=int(rinv[2])*4
    s4=int(rinv[3])*5
    s5=int(rinv[4])*6
    s6=int(rinv[5])*7
    s7=int(rinv[6])*2
    s8=int(rinv[7])*3

    suma = s1+s2+s3+s4+s5+s6+s7+s8
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
    s1=int(rinv[0])*2
    s2=int(rinv[1])*3
    s3=int(rinv[2])*4
    s4=int(rinv[3])*5
    s5=int(rinv[4])*6
    s6=int(rinv[5])*7
    s7=int(rinv[6])*2

    suma = s1+s2+s3+s4+s5+s6+s7
    resto = suma%11
    digver = 11-resto

    if digver==10:
        print("Su dígito verificador es:" ,'dv=k')
    elif digver==11:
        print("Su dígito verificador es:" ,'dv=0')
    else:
        print("Su dígito verificador es:",'dv=3')
