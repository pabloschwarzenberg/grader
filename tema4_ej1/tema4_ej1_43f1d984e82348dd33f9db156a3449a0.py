def ocultar_letras(palabra,cantidad):
    import random
    palabra1=list(palabra)
    while cantidad>0:
        j=random.randint(0,(len(palabra)-1))
        if palabra1[j]!="_":
            palabra1[j]="_"
            cantidad-=1
        else:
            cantidad+=0
    palabra_secreta="".join(palabra1)
    if cantidad==0:
        return palabra_secreta

def revisar_letra(palabra,palabra_secreta,letra):
    if letra==palabra:
        return palabra
    a=palabra_secreta.count("_")
    while a>0 and letra in palabra:
            b=palabra.find(letra)
            if palabra_secreta[b]=="_":
                palabra_secreta1=list(palabra_secreta)
                palabra_secreta1[b]=letra
                palabra_secreta="".join(palabra_secreta1)
                palabra1=list(palabra)
                palabra1[b]="."
                palabra="".join(palabra1)
                a-=1
            else:
                palabra1=list(palabra)
                palabra1[b]="."
                palabra="".join(palabra1)
                a+=0
    return palabra_secreta



if __name__ == "__main__":
    pass
         