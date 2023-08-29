#Cálculo del dígito verificador de un rut
print("Vamos a calcular el digito verificador del rut")
rut = str(input("Ingrese su rut sin el dígito verificador, ni puntos:"))
if len(rut)==8:
    rinv = rut[::-1]
    a1=int(rinv[0])*2
    a2=int(rinv[1])*3
    a3=int(rinv[2])*4
    a4=int(rinv[3])*5
    a5=int(rinv[4])*6
    a6=int(rinv[5])*7
    a7=int(rinv[6])*2
    a8=int(rinv[7])*3

    sumatoria = a1+a2+a3+a4+a5+a6+a7+a8
    resto = sumatoria%11
    dig_verificador = 11-resto

    if dig_verificador==10:
        print("Su dígito verificador es:" ,'dv=K')
    elif dig_verificador==11:
        print("Su dígito verificador es:" ,'dv=0')
    else:
        print("Su dígito verificador es:",'dv=3')

elif len(rut)==7:
    rinv = rut[::-1]
    a1=int(rinv[0])*2
    a2=int(rinv[1])*3
    a3=int(rinv[2])*4
    a4=int(rinv[3])*5
    a5=int(rinv[4])*6
    a6=int(rinv[5])*7
    a7=int(rinv[6])*2

    sumatoria = a1+a2+a3+a4+a5+a6+a7
    resto = sumatoria%11
    dig_verificador = 11-resto

    if dig_verificador==10:
        print("Su dígito verificador es:" ,'dv=k')
    elif dig_verificador==11:
        print("Su dígito verificador es:" ,'dv=0')
    else:
        print("Su dígito verificador es:",'dv=3')