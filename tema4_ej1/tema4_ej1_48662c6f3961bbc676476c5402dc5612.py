def ocultar_letras(palabra,cantidad):

    posiciones = []
    import random
    while len(posiciones) < cantidad:
        n = random.randint(1, len(palabra) - 1)
        if n not in posiciones:
            posiciones.append(n)

    lista = list(palabra)
    for i in range(len(posiciones)):
        lista[posiciones[i]] = '_'

    palabra = ''.join(lista)

    return palabra 



def revisar_letra(palabra_secreta,palabra,letra):

    if letra in palabra_secreta:
        lista = list(palabra)
        for i in range(len(palabra)):
            if lista[i] == "_" and palabra_secreta[i] == letra:
                lista[i] = letra

        palabra = ''.join(lista)
        return palabra
    
    else:
        return palabra