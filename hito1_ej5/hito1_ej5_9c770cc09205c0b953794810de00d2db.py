#Codigo Verificador
rut=int(input("Ingrese un rut de 8 digitos:"))
posiciones=7
indice=1
Numero=rut
serie=7 # 2 3 4 5 6 7 2 3
Suma=0
while indice <= 8 :
    digito= int(Numero // 10**posiciones)
    if indice==1 or indice==2 :
        if indice==1:
            Suma+=digito*3
        else :
            Suma+=digito*2
    else :
        Suma+=digito*serie
        serie-=1
    Numero=Numero-digito*10**posiciones
    posiciones-=1
    indice+=1
resto=Suma % 11
verificador=11- (Suma % 11)
if verificador == 11 :
    verificador=0
else :
    if verificador==10 :
        verificador="k"
print("dv="+str(verificador))