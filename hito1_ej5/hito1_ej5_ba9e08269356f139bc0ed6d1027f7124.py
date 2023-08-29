rut=str(input("Ingresa ru Rut , sin puntos ni digito verificador: "))
rut=rut[::-1]
val="23456723"
tamaño=len(rut)
indiceVal=0 #contador de Val
indice=0 #contador de rut
valResultado=1
resultado=0

while int(rut)>0:           
            resultado=(int(rut[indice])* int(val[indiceVal]))+resultado
            valResultado=resultado
            indice+=1
            indiceVal+=1
            if indice==int(tamaño) :
                  break
divEnt=resultado// 11
modulo=resultado-(11*divEnt)
resta=11-modulo
if  resta== 11:
    dv=0
if resta==10:
    dv="k"
if resta!=11 and resta!=10:
    dv=resta

print("dv=",dv )