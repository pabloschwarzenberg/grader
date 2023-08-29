import random

def ocultar_letras(palabra,cantidad):
    rndm=[]
    for i in range(0,cantidad):
        count = 0
        while count !=1:
            x=random.randint(0,len(palabra)-1)
            b=0
            for j in range(0,len(rndm)):
                if rndm[j]== x:
                    b=1
            if b!=1:
                rndm.append(x)
                count=1
    for i in range(0,len(rndm)):
        lp=list(palabra)
        lp[rndm[i]]= "_"
        palabra="".join(lp)
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    g=list(palabra)
    for i in range(0,len(g)):
        if g[i]=="_":
            if palabra_secreta[i]==letra:
                g[i]= letra
        palabra= "".join(g)
    return palabra
