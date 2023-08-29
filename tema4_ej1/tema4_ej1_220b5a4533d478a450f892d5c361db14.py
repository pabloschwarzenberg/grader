from random import randint

palab="lepidoptero"

def ocultar_letras(palab, cant):
    palab=list(palab)
    L=[]
    while cant != 0:
        a = randint(1,len(palab)-1)
        if a not in L:
         L.append(a)
         palab[a] = "_"
         cant-= 1
    palab="".join(palab)
    return palab

def revisar_letra(palab_secret,palab,let):
    a = list(palab_secret)
    palab=list(palab)
    if let in a:
        x=palab_secret.find("-")
        palab[x] = let
    palab="".join(palab)

    return palab