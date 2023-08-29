#Cálculo del dígito verificador de un rut
rut=int(input("ingrese el numero del rut: "))
digitosDelRut=len(str(rut))
serieNumerica=2
suma=0
while digitosDelRut>0:
    componente=rut%10
    rut=(rut-componente)/10
    multiplicacion=componente*serieNumerica
    if serieNumerica==7:
        serieNumerica=1
    suma+=multiplicacion
    serieNumerica+=1
    digitosDelRut-=1
restoDivicion=suma//11
restoDivicionEntera=suma-(11*restoDivicion)
resto=11-restoDivicionEntera
if resto==10:
    dv="k"
elif resto==11:
    dv=0
else:
    dv=resto
print("dv="+str(dv))      