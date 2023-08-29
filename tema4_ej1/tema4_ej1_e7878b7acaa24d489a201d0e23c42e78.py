import random
def ocultar_letras(palabra,cantidad):
    while cantidad>0:
        x=random.randint(0,(len(palabra)-1))
        if palabra[x]!="_":
            palabra=palabra.replace(palabra[x],"_",1)
            cantidad-=1
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    contador=0
    while contador<len(palabra_secreta):
        if letra==palabra_secreta[contador]:
            if palabra[contador]=="_":
                palabra=palabra[:contador]+letra+palabra[contador+1:]
        contador+=1
    return palabra

if __name__ == "__main__":
    pass
         