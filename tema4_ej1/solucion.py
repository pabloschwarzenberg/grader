import random
palabras=["camion","lepidoptero","rinoceronte"]

#reemplaza aleatoriamente algunas letras de la palabra por _
def ocultar_letras(palabra,cantidad):
    palabra=list(palabra)
    d=list(range(len(palabra)))
    while cantidad>0:
        p=random.choice(d)
        palabra[p]="_"
        d.remove(p)
        cantidad-=1
    return "".join(palabra)

def revisar_letra(palabra_secreta,palabra,letra):
    palabra=list(palabra)
    if letra in palabra_secreta:
        for i in range(len(palabra)):
            if palabra_secreta[i]==letra:
                palabra[i]=letra
    palabra="".join(palabra)
    return palabra

if __name__ == "__main__":
    palabra_secreta=palabras[1]
    incognitas=len(palabra_secreta)//2
    palabra=ocultar_letras(palabra_secreta,incognitas)
    print(palabra)
    print(revisar_letra(palabra_secreta,palabra,"j"))
    print(revisar_letra(palabra_secreta,palabra,"o"))
