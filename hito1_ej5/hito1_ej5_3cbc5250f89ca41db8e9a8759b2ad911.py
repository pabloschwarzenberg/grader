#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese un rut de 8 digitos:"))
posiciones=7
indice=1
numero=rut
serie=7 # 2 3 4 5 6 7 2 3
suma=0
while indice <=8:
    digito=int(numero//10**posiciones)
    if indice==1 or indice==2:
        if indice==1:
            suma+=digito*3
        else:
            suma+=digito*2
    else:
        suma+=digito*serie
        serie-=1
    numero=numero-digito*10**posiciones
    posiciones-=1
    indice+=1
resto=suma%11
verificador=11-(suma%11)
if verificador ==11:
    verificador=0
else:
    if verificador==10:
        verificador="K"
print("dv="+str(verificador))
