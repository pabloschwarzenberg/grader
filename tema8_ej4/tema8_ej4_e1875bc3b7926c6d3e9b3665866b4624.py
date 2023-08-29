def rot13(palabra) :
    abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                  "u", "v", "w", "x", "y", "z"]

    lista_palabra=list(palabra)
    pos_letra = []
    palabra_cifrada=[]
    for i in lista_palabra :
        pos_letra_abc=abecedario.index(i)
        if pos_letra_abc <= 12 :
                numero_de_letra=(pos_letra_abc+13)
                pos_letra.append(numero_de_letra)
        else :
            numero_de_letra=(pos_letra_abc-13)
            pos_letra.append(numero_de_letra)
    for i in pos_letra :
        carac_cifrado=abecedario[i]
        palabra_cifrada.append(carac_cifrado)
        resultado="".join(palabra_cifrada)

    return resultado