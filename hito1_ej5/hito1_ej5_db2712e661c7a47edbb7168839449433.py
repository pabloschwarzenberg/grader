#Cálculo del dígito verificador de un rut
rut=int(input("Introduzca su rut sin dígito verificador: "))

if rut >= 1 and rut <= 99999999:
    dig1= rut % 10
    dig1= dig1 * 2
    
    dig2= rut // 10
    dig2= dig2 % 10
    dig2= dig2* 3
    
    dig3= rut // 100
    dig3= dig3 % 10
    dig3= dig3 * 4

    dig4= rut // 1000
    dig4= dig4 % 10
    dig4= dig4 * 5

    dig5= rut // 10000
    dig5= dig5 % 10
    dig5= dig5 * 6

    dig6= rut // 100000
    dig6= dig6 % 10
    dig6= dig6 * 7

    dig7= rut // 1000000
    dig7= dig7 % 10
    dig7= dig7 * 2

    dig8= rut // 10000000
    dig8= dig8 % 10
    dig8= dig8 * 3
    

    suma= dig1 + dig2 + dig3 + dig4 + dig5 + dig6 + dig7 + dig8
    suma= suma % 11
    dv= 11 - suma

    if dv == 11:
        print("dv=0")

    elif dv == 10:
        print("dv=K")

    else:
        print("dv=",dv)