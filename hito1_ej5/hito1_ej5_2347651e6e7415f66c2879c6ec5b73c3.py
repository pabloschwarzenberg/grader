#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese rut para calcular codigo verificador: "))

rut1=(rut%10)*2
rut2=((rut%100-rut%10)/10)*3
rut3=((rut%1000-rut%100)/100)*4
rut4=((rut%10000-rut%1000)/1000)*5
rut5=((rut%100000-rut%10000)/10000)*6
rut6=((rut%1000000-rut%100000)/100000)*7
rut7=((rut%10000000-rut%1000000)/1000000)*2
rut8=((rut%100000000-rut%10000000)/10000000)*3

rutTl=(rut1+rut2+rut3+rut4+rut5+rut6+rut7+rut8)
rutTl2=int((rutTl/11))
rutCV=round(rutTl-(11*rutTl2),1)
rutCV1=(11-rutCV)

if rutCV1==11:
    print("dv = 0")  
elif rutCV1==10:
    print("dv = K")
else:
    print("dv","=",round(rutCV1))
