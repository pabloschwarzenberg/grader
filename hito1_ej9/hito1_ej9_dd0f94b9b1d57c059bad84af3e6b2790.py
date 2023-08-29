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