import random
def ocultar_letras(pala,esconde):
    pal=list(pala)
    numeros=[]
    for c in range(0, len(pal)):
            numeros.append(c)
            random.shuffle(numeros)
            
    for i in range(0, esconde):
        bur=numeros[i]
        pal[bur]="_"
    palabra="".join(pal)
    return palabra

def revisar_letra(palabra, escondida, letra):
    if letra in palabra:
        pal=list(palabra)
        esc=list(escondida)
        for i in range(0, len(esc)):
            if esc[i]=="_":
                if pal[i]==letra:
                    esc[i]=letra
                else:
                    continue
        palfinal="".join(pal)
        escfinal="".join(esc)
        return escfinal
    else:
        return False

if __name__ == "__main__":
    pass
         