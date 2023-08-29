import random
def ocultar_letras(palabra,cantidad):
    lista = []
    p = list(palabra)
    size = len(palabra)
    n = 0

    while n < cantidad:
        x = random.randint(0,size-1)
        if x < size:
            if x not in lista:
                lista.append(x)
                n += 1

    for posicion in lista:
        p[posicion] = '_'

    palabra = "".join(p)
    
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    secreta = list(palabra_secreta)
    palabra = list(palabra)

    lista = []
    
    for e in range(len(secreta)):
        if secreta[e] == letra:
            lista.append(e)

    for i in lista:
        if palabra[i] == '_':
            palabra[i] = letra      

    palabra = "".join(palabra)      
    
    return palabra
         