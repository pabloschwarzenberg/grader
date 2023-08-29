#Descomponer un número

print("descomponer numeros")
tira=""
numero=int(input("ingrese numero de 4 digitos: "))
aux_numero=numero
unidades= int(numero//10**3)
numero=numero-unidades*10**3
centena=int(numero//10**2)
numero=numero-centena*10**2
decena=int(numero//10**1)
numero=numero-decena*10**1
unidad=int(numero)
if aux_numero>=999:
    tira=tira+str(unidades)+"M"+"+"+str(centena)+"C"+"+" +str(decena)+"D"+"+" +str(unidad)+"U"
else:
    if aux_numero>=99:
        tira=tira+str(centena)+"C"+"+"+str(decena)+"D"+ "+"+str(unidad)+"U"
    else:
        if aux_numero>=9:
            tira=tira+str(decena)+"D"+"+"+str(unidad)+"U"
        else:
            tira=tira+str(unidad)+"U"
            
print(tira)     