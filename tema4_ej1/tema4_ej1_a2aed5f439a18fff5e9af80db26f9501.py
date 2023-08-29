import random

def ocultar_letras(palabra_secreta, cantidad):
    a_l = list(palabra_secreta)
    y = random.randint(0, len(a_l) - 1)
    y_l = list(str(y))
    for i in range(cantidad):
        y = random.randint(0, len(a_l)-1)
        while str(y) in y_l:
            y = random.randint(0, len(a_l) - 1)

        else:
            a_l[y] = "_"
            y_l.append(str(y))

    palabra = "".join(a_l)
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    a_l = list(palabra_secreta)
    as_l = list(palabra)
    palabra1 = "".join(as_l)
    intentos = 6
    for i in range(len(a_l)):
        if a_l[i] == letra:
            as_l[i] = letra
    palabra1 = "".join(as_l)
    if  palabra_secreta != palabra1:
        return palabra1

    while palabra_secreta != palabra1 and intentos > 0:
        if __name__ == "__main__":
            letra1 = str(input())
            for i in range(len(a_l)):
                if a_l[i] == letra1:
                    as_l[i] = letra1
            palabra1 = "".join(as_l)
            intentos = intentos - 1
            return palabra1


    if palabra_secreta == palabra1:
        return "ganaste, la palabra secreta era:", palabra_secreta
    if intentos == 0:
        return "perdiste, la palabra secreta era:", palabra_secreta




if __name__ == "__main__":
    palabras = ["murcielago", "lepidoptero", "postre", "pisco","lepidoptero","lepidoptero","lepidoptero"]
    palabra_secreta = (random.choice(palabras))
    cantidad = random.randint(1, len(palabra_secreta)-1)
    palabra = (ocultar_letras(palabra_secreta, cantidad))
    print(palabra)
    intentos = 6
    letra = str(input())
    print(revisar_letra(palabra_secreta, palabra, letra))





