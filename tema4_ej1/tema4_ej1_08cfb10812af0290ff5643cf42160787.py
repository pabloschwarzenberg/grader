import random
def ocultar_letras(palabra,cantidad):
    i=0
    posibles=list(range(len(palabra)))
    for i in range(i,cantidad):
        ocultar_letra = random.choice(posibles)
        posibles.remove(ocultar_letra)
        letra=palabra[ocultar_letra]
        palabra=palabra.replace(letra,"_",1)
    return palabra

def revisar_letra(palabra,palabra_secreta,letra):
    ii=0
    palabra_secreta_como_lista=list(palabra_secreta)
    if len(letra)==1:
        while ii < len(palabra):
            letras_de_la_palabra=list(palabra)
            if letra in letras_de_la_palabra[ii:]:
                letra_encontrada=letras_de_la_palabra.index(letra,ii)
                palabra_secreta_como_lista[letra_encontrada]=letra
            ii=ii+1
    elif len(letra)>1 and palabra==letra:
        palabra_secreta=palabra
        return palabra
    return "".join(palabra_secreta_como_lista)

if __name__ == "__main__":
    palabra=input()
    cantidad=int(input())
    palabra_secreta=ocultar_letras(palabra,cantidad)
    print(palabra_secreta)
    letra=input()
    print(revisar_letra(palabra,palabra_secreta,letra))