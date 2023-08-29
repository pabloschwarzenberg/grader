rut=str(input("Ingrese su Rut sin dígito verificador: "))
l= len(rut)
i = l-1
suma=0
c=0
div=0
dv=0
if l == 8:
    suma+= int(rut[7])*2
    suma+= int(rut[6])*3
    suma+= int(rut[5])*4
    suma+= int(rut[4])*5
    suma+= int(rut[3])*6
    suma+= int(rut[2])*7
    suma+= int(rut[1])*2
    suma+= int(rut[0])*3
    div = suma%11
    dv=11-div
    if dv == 11:
        dv=0
    elif dv==10:
        dv="K"
    print("dv=",dv)

if l == 7:
    suma+= int(rut[6])*2
    suma+= int(rut[5])*3
    suma+= int(rut[4])*4
    suma+= int(rut[3])*5
    suma+= int(rut[2])*6
    suma+= int(rut[1])*7
    suma+= int(rut[0])*2
    div = suma%11
    dv=11-div
    if dv==11:
        dv=0
    elif dv == 10:
        dv="K"
    print("dv=",dv)   