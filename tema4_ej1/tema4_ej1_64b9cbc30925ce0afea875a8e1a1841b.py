from random import randint,choice
def ocultar_letras(palabra,cantidad):
    largo = len(palabra)
    palabra_lista = list(palabra)
    for i in range(1, cantidad+1):
        n = randint(0, largo-1)
        if palabra_lista[n] == "_":
            a = randint(0, largo-1)
            for e in palabra_lista:
                if e == "_":
                    pass
                else:
                    e == "_"
        else:
            palabra_lista[n] = "_"
    palabra_escondida = "".join(palabra_lista)
    return palabra_escondida

def revisar_letra(palabra_secreta,palabra,letra):
    lista_secreta = list(palabra_secreta)
    lista_palabra = list(palabra)
    largo = len(palabra_secreta)
    veces = palabra_secreta.count(letra)
    c = 0
    lista_de = []
    g = 0
    if veces>0:
        for i in range(1, veces+1):
            a = palabra_secreta[c:].find(letra)+c
            c = a+1
            lista_de.append(a)

        while g<veces:
            lista_palabra[lista_de[g]] = letra
            g = g+1
    else:
        pass
    palabraf = "".join(lista_palabra)
    return palabraf

if __name__ == "__main__":
    pass
         