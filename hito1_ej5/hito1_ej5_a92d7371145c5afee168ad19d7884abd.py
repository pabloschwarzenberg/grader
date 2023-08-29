#Cálculo del dígito verificador de un rut
rut=input("ingresar rut  sin codigo verigicador")
if len(rut)==8:
    suma=int(rut[7])*2+int(rut[6])*3+int(rut[5])*4+int(rut[4])*5+int(rut[3])*6+int(rut[2])*7+int(rut[1])*2+int(rut[0])*3
    dv=11-(int(suma)-(11*(int(suma)//11)))
    if dv == 11:
        dv="0"
        print("dv=",dv)
    elif dv==10:
        dv="k"
        print("dv=",dv)
    else:
        print("dv=",dv)
if len(rut)==7:
    suma=int(rut[6])*2+int(rut[5])*3+int(rut[4])*4+int(rut[3])*5+int(rut[2])*6+int(rut[1])*7+int(rut[0])*2
    dv=11-(int(suma)-(11*(int(suma)//11)))
    if dv == 11:
        dv="0"
        print("dv=",dv)
    elif dv==10:
        dv="k"
        print("dv=",dv)
    else:
        print("dv=",dv)
        
        
        