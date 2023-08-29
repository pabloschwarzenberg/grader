#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese el rut a validar:"))
posi=7
marcador=1
numero=rut
serie=7
suma=0
while marcador <= 8 :
    dv= int(numero // 10**posi)
    if marcador ==1 or marcador==2 :
        if marcador==1 :
            suma+=dv*3
        else :
            suma+=dv*2
    else :
        suma+=dv*serie
        serie-=1
    numero=numero-dv*10**posi
    posi-=1
    marcador+=1
resto=suma % 11
marca_verif=11- (suma % 11)
if marca_verif == 11 :
    marca_verif=0
else :
    if marca_verif ==10 :
        marca_verif="K"
print("dv=",marca_verif)
