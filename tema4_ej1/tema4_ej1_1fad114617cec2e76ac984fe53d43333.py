import random
listasecretas=["lepidoptero","sofita","olla"]
cual=random.randint(0,len(listasecretas)-1)
palabrasecreta=listasecretas[cual]
nomostrar=random.randint(1,len(palabrasecreta))

def ocultar_letras(palabra1,cantidad):
    ocultar=list(palabra1)
    i=0
    while i<cantidad:
        if ocultar[i]!="_":
            ocultar[i]="_"
            i=i+1
    nueva="".join(ocultar)
    return nueva

def revisar_letra(palabra_secreta,palabra2,letra):
    palabra3=list(palabra2)
    j=0
    while j<len(palabra_secreta):
        if palabra_secreta[j]==letra:
            palabra3[j]=letra
        j+=1
    nueva2="".join(palabra3)
    return nueva2

if __name__ == "__main__":
    pass
         