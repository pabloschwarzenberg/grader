import random

def ocultar_letras(palabra,cantidad):
    l=len(palabra)
    pal=list(palabra)
    for i in range(cantidad+1):
        n=random.randint(0,l)
        pal.pop(n)
        pal.insert(n,"_")
    palabra="".join(pal)
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    ps=list(palabra_secreta)
    pm=list(palabra)
    j=[]
    c=len(palabra)
    for i in range(c):
        if ps[i]==letra:
            j.append(letra)
        else:
            g=pm[i]
            j.append(g)
    palabra="".join(j)
    return palabra


if __name__ == "__main__":
    pass
         