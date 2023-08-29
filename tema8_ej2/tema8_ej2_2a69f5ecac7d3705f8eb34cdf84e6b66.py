def buscarTodas(a,b):
    cadena=""
    cont=0
    for w in a:
        if (w == b):
                cadena=cadena+str(cont)+" "
        cont=cont+1
    valor=list(cadena)
    valor.pop()
    sear=""
    for tt in valor:
        sear=sear+tt
    return sear
