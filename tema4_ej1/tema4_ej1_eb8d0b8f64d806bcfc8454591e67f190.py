from random import randint
def ocultar_letras(palabra,cantidad):
    palabra2=list(palabra)
    while cantidad!=0:
        a=randint(0,(len(palabra))-1)
        while True:
            if palabra2[a]=="_":
                a=randint(0,(len(palabra))-1)
                continue
            else:
                palabra2[a]="_"
                cantidad=cantidad-1
                break
    palabra="".join(palabra2)
    return palabra
def revisar_letra(palabra_secreta,palabra,letra):
    palabra2=list(palabra)
    palabra_secreta2=list(palabra_secreta)
    lista=""
    d=0
    for b in palabra2:
        if b=="_":
            lista=lista+palabra_secreta2[d]
            d=d+1
        else:
            lista=lista+"_"
            d=d+1
    lista="".join(lista)
    h=lista.find(letra)
    if h==-1:
        pass
    else:
        palabra2[h]=letra
        palabra="".join(palabra2)
        return palabra
    pass

if __name__ == "__main__":
    pass
         