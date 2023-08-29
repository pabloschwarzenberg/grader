from random import randrange
def ocultar_letras(palabra_secreta,cantidad):
    longitud=len(palabra_secreta)
    indice=0
    palabra=list(palabra_secreta)
    cantidad=int(cantidad)
    while cantidad>0:
        indice=randrange(longitud)
        if palabra[indice]=="_":
            cantidad=cantidad+0
        else:
            palabra[indice]="_"
            cantidad-=1
    palabra="".join(palabra)
    return palabra
def revisar_letra(palabra_secreta,palabra,letra):
    if palabra_secreta==letra:
        return palabra_secreta
    long1=len(palabra_secreta)
    long2=len(letra)
    if long1==long2:
        print("Has fallado")
        return print("Lo correcto era:",palabra_secreta)
    veces=palabra_secreta.count(letra)
    veces=int(veces)
    palabra=list(palabra)
    if veces>=1:
        indice=0
        while indice < len(palabra_secreta):
            indice_letra = palabra_secreta[indice]
            if indice_letra == letra:
                palabra[indice] = letra
            indice += 1
    return ("".join(palabra))