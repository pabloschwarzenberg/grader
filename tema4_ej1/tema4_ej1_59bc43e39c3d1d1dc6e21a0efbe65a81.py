from random import randint
pal= "lepidoptero"
def ocultar_letras(pal, cant):
    pal = list(pal)
    lista=[]
    while cant != 0:
        a = randint(1, len(pal) - 1)
        if a not in lista:
         lista.append(a)
         pal[a]= "_"
         cant-=1
    pal= "".join(pal)
    return pal

def revisar_letra(ps, pal, letra):
    a=list(ps)
    pal= list(pal)
    if letra in a:
        x=ps.find("-")
        pal[x]=letra
    pal= "".join(pal)

    return pal