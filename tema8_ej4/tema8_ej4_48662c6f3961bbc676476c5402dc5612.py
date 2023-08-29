def rot13(palabra):
    grupo1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', ' ']
    grupo2 = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

    lista = list(palabra)

    for i in range(len(lista)):
        if lista[i] in grupo1:
            x = grupo1.index(lista[i])
            lista[i] = grupo2[x]
        
        elif lista[i] in grupo2:
            x = grupo2.index(lista[i])
            lista[i] = grupo1[x]

    palabra = ''.join(lista)
    return palabra