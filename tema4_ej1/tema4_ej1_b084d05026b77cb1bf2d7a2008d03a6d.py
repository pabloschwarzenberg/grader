import random
def ocultar_letras(palabra,cantidad):
    word = list(palabra)
    largo= len(word)
    l=[]
    posicion = random.randint(0, largo -1)
    l.append(posicion)
    word[posicion]= "_"
    a= len(l)
    while a < cantidad:
        repite = se_repite(posicion, l)
        while repite:
            posicion = random.randint(0, largo -1)
            repite = se_repite(posicion, l)
        l.append(posicion)
        word[posicion]= "_"
        a= len(l)
    word= "".join(word)
    return word

def se_repite(numero, lista):
    for i in range(0, len(lista)):
            if lista[i]== numero:
                repite= True
                break
            else:
                repite= False
    return repite

def revisar_letra(palabra_secreta,palabra,letra):
    if len(letra)== len(palabra_secreta):
        if letra == palabra_secreta:
            palabra = palabra_secreta
    elif len(letra)==1:
        l = encontrar_letra(palabra_secreta,letra)
        palabra = list(palabra)
        for i in range(0, len(l)):
            if palabra[l[i]] == "_":
                palabra[l[i]] = letra
        palabra= "".join(palabra)
    return palabra


def encontrar_letra(palabra_secreta,letra):
    l=[]
    palabra_secreta = list(palabra_secreta)
    for i in range(0, len(palabra_secreta)):
        if palabra_secreta[i]== letra:
            l.append(i)
    return l

if __name__ == "__main__":
    pass
         