print ("Descomponer un número")
tira=""
numero=int(input("Ingrese un núumero de 4 digitos:"))
auxNumero=numero
unidades= numero // 10**3
numero=numero-unidades*10**3
centena= numero // 10**2
numero=numero-centena*10**2
decena= numero // 10**1
numero=numero-decena*10**1
unidad= numero
if auxNumero>=999 :
    tira=tira+str(unidades)+"M"+" + "+str(centena)+"C"+" + " + str(decena)+"D"+" + "+str(unidad)+"U"
else :
    if auxNumero>=99 :
        tira=tira+str(centena)+"C"+" + " + str(decena)+"D"+" + "+str(unidad)+"U"
    else :
        if auxNumero>=9 :
            tira=tira+str(decena)+"D"+" + "+str(unidad)+"U"
        else :
            tira=tira+str(unidad)+"U"

print(tira)