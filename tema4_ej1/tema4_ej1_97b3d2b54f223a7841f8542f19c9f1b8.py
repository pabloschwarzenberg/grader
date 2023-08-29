def ocultar_letras(palabra,cantidad):
    if len(palabra)>0:
        for idx in range(len(palabra)):
            if cantidad==palabra[idx]:
                return 1
        palabra.append(int(cantidad))
    else:
        palabra.append(int(cantidad))
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    pos=0
    indicador=0

    for l in palabra_secreta:
        if letra==l:
            pos=palabra_secreta.index(l,pos)
            palabra[pos]=letra
            pos=pos+1
            indicador=1

    if indicador==0:
        return True
    return palabra
