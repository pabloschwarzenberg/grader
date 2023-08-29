import random
def ocultar_letras(palabra,cantidad):
    x=0
    adiv=palabra
    while x<cantidad:
        a=random.randint(0,len(adiv)-1)
        adiv=list(adiv)
        if adiv[a]=='_':
            x-=1
        adiv[a]='_'
        x+=1
    global adiv
    adiv=''.join(adiv)
    print (adiv)
    return adiv

def revisar_letra(palabra_secreta,palabra,letra):
    if len(letra)>1:
        if letra==palabra_secreta:
            return palabra_secreta
        else:
            return palabra
    n=0
    while palabra_secreta.find(letra,n)!=-1:
        a=palabra_secreta.find(letra,n)
        palabra=list(palabra)
        palabra[a]=letra
        palabra=''.join(palabra)
        print (palabra)
        n+=1
    print (palabra)
    return palabra

if __name__ == "__main__":
    pass
         