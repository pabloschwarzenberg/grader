import random
def ocultar_letras(palabra,cantidad):
    x = 0
    while x < cantidad:
        a = random.randrange(len(palabra))
        if palabra[a] == "_":
            continue
        else:
            palabra = palabra.replace(palabra[a],"_",1)
            x = x + 1
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    a = list(palabra_secreta)
    b = list(palabra)
    if palabra_secreta == letra:
        return palabra_secreta
    elif palabra_secreta.find(letra) == -1:
        return -1
    else:
        for i in range(len(b)):
            if b[i] == "_":
                if a[i] == letra:
                    b[i] = a[i]
        return "".join(b)

         