def rot13(palabra):
    palabra = palabra.lower()
    abecedario = list(map(chr,range(97,123)))
    lista =[]
    for i in range(len(palabra)):
        posicion = abecedario.index(palabra[i])
        letra_rot = abecedario[posicion-13]
        lista.append(letra_rot)
    palabra = "".join(lista)   
    return palabra


           