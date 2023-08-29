import string
alfabeto=list(string.ascii_lowercase)
def cifradoCesar(alfabeto,n,texto):
    textoCifrado=""
    for letra in texto:
        if letra in alfabeto:
            indiceActual=alfabeto.index(letra)
            indiceCesar=indiceActual+n
            if indiceCesar>25:
                indiceCesar-=25
            textoCifrado+=alfabeto[indiceCesar]
        else:
            textoCifrado+=letra
    return textoCifrado

           