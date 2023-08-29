rut = str(input("Ingrese su rut sin dígito verificador, ni puntos:"))
if len(rut) == 8:
    rinv = rut[::-1]
    num1=int(rinv[0])*2
    num2=int(rinv[1])*3
    num3=int(rinv[2])*4
    num4=int(rinv[3])*5
    num5=int(rinv[4])*6
    num6=int(rinv[5])*7
    num7=int(rinv[6])*2
    num8=int(rinv[7])*3

    suma = num1+num2+num3+num4+num5+num6+num7+num8
    resto = suma % 11
    digito = 11-resto

    if digito == 10:
        print("dv=k")
    elif digito == 11:
        print("dv=0")
    else:
        print("dv=",digito)

elif len(rut)==7:
    rinv = rut[::-1]
    num1=int(rinv[0])*2
    num2=int(rinv[1])*3
    num3=int(rinv[2])*4
    num4=int(rinv[3])*5
    num5=int(rinv[4])*6
    num6=int(rinv[5])*7
    num7=int(rinv[6])*2

    suma = num1+num2+num3+num4+num5+num6+num7
    resto = suma%11
    digito = 11-resto

    if digito==10:
        print("dv=k")
    elif digito==11:
        print("dv=0")
    else:
        print("dv=",digito)