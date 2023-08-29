#Descomponer un número
print ("Descomponer un número")
Tira=""
Numero=int(input("Ingrese un núumero de 4 digitos:"))
Aux_Numero=Numero
Unidades= int(Numero // 10**3)
Numero=Numero-Unidades*10**3
Centena= int(Numero // 10**2)
Numero=Numero-Centena*10**2
Decena= int(Numero // 10**1)
Numero=Numero-Decena*10**1
Unidad= int(Numero)
if Aux_Numero>=999 :
    Tira=Tira+str(Unidades)+"M"+" + "+str(Centena)+"C"+" + " + str(Decena)+"D"+" + "+str(Unidad)+"U"
else :
    if Aux_Numero>=99 :
        Tira=Tira+str(Centena)+"C"+" + " + str(Decena)+"D"+" + "+str(Unidad)+"U"
    else :
        if Aux_Numero>=9 :
            Tira=Tira+str(Decena)+"D"+" + "+str(Unidad)+"U"
        else :
            Tira=Tira+str(Unidad)+"U"

print(Tira)      