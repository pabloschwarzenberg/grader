rut = int(input("Introdusca rut sin N°verificador ni puntos:"))#30686957
rutInvert = str(rut)[::-1]
if(len(rutInvert)==8):
    rutInvert = int(rutInvert*1)
    rut1 = (rutInvert//10000000)*2
    rut2 = ((rutInvert//1000000)%10)*3
    rut3 = ((rutInvert//100000)%10)*4
    rut4 = ((rutInvert//10000)%10)*5
    rut5 = ((rutInvert//1000)%10)*6
    rut6 = ((rutInvert//100)%10)*7
    rut7 = ((rutInvert//10)%10)*2
    rut8 = (rutInvert%10)*3
    suma = rut1+rut2+rut3+rut4+rut5+rut6+rut7+rut8
    modulo = suma//11
    resto = suma-(11*modulo)
    final = 11-resto
    if(final==11):
        print("dv=0")
    elif(final==10):
        print("dv=K")
    else:
        print("dv=",final)
elif(len(rutInvert)==7):
    rutInvert = int(rutInvert*1)
    rut1 = (rutInvert//1000000)*2
    rut2 = ((rutInvert//100000)%10)*3
    rut3 = ((rutInvert//10000)%10)*4
    rut4 = ((rutInvert//1000)%10)*5
    rut5 = ((rutInvert//100)%10)*6
    rut6 = ((rutInvert//10)%10)*7
    rut7 = (rutInvert%10)*2
    suma = rut1+rut2+rut3+rut4+rut5+rut6+rut7
    modulo = suma//11
    resto = suma-(11*modulo)
    final = 11-resto
    if(final==11):
        print("dv=0")
    elif(final==10):
        print("dv=K")
    else:
        print("dv=",final)