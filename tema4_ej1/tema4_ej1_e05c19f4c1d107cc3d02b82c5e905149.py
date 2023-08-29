from random import randint

def ocultar_letras(palabra, cantidad):
    palabra = list(palabra)

    while cantidad != 0:
        n = randint(0, len(palabra) - 1)
        if palabra[n] != '_':
            cantidad -= 1
            palabra[n] = '_'

    return ''.join(palabra)


def revisar_letra(palabra_secreta, palabra, letra):
    palabra_secreta = list(palabra_secreta)

    if len(letra) == 1:
        for i in range(len(palabra)):
            if palabra[i] == letra:
                palabra_secreta[i] = letra

        return ''.join(palabra_secreta)

    else:
        if palabra == letra:
            return palabra


if __name__ == "__main__":
    pass
    #print(revisar_letra('le_i_opter_ ', 'lepidoptero', 'o'))
