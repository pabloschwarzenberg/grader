#Cálculo del dígito verificador de un rut
Rut=input("Ingrese Rut sin puntos y sin digito verificador: ")
caracteres=str(Rut)
dig=len(caracteres)
if dig==8:
    dig8= int(caracteres[7])*2
    dig7= int(caracteres[6])*3
    dig6= int(caracteres[5])*4
    dig5= int(caracteres[4])*5
    dig4= int(caracteres[3])*6
    dig3= int(caracteres[2])*7
    dig2= int(caracteres[1])*2
    dig1= int(caracteres[0])*3
    suma=dig8+dig7+dig6+dig5+dig4+dig3+dig2+dig1
    div=suma//11
    mult=div*11
    rest=suma-mult
    dv=11-rest
if dig==7:
    dig7= int(caracteres[6])*2
    dig6= int(caracteres[5])*3
    dig5= int(caracteres[4])*4
    dig4= int(caracteres[3])*5
    dig3= int(caracteres[2])*6
    dig2= int(caracteres[1])*7
    dig1= int(caracteres[0])*2
    suma=dig7+dig6+dig5+dig4+dig3+dig2+dig1
    div=suma//11
    mult=div*11
    rest=suma-mult
    dv=11-rest
if dv==11:
    dv=0
elif dv==10:
    dv='k'
else:
    dv=dv
print("dv=",dv)
 
    

     