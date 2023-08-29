import random
def ocultar_letras(palabra,cantidad):
    cantidad_pal=len(palabra)
    pal=list(palabra)    
    while cantidad > 0:

        posicion=random.randrange(1,cantidad_pal)

        if pal[posicion-1]!="_":
            pal[posicion-1]="_"
            cantidad-=1 
    palabra=''.join(pal) 
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    cantidad_sec=len(palabra_secreta)
    letra_encontrada=0
    pal=list(palabra)
    for n in range(0,cantidad_sec):
    
        if palabra_secreta[n]==letra:

            letra_encontrada=1

    if letra_encontrada == 1:
        
        for n in range(0,cantidad_sec):
            if palabra_secreta[n]==letra:
                pal[n]=letra
    palabra=''.join(pal) 
    return palabra

