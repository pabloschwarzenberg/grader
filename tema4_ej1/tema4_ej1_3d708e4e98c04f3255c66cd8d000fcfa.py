from random import choice


def ocultar_letras(palabra, cantidad):
    count = 0
    palabra = [x for x in palabra]
    while count < cantidad:
        while True:
            char = choice(palabra)
            if "_" in palabra:
                if char != "_":
                    palabra[palabra.index(char)] = "_"
                    break
                else:
                    break
            else:
                palabra[palabra.index(char)] = "_"
                break
        count += 1
    return "".join(palabra)


def revisar_letra(palabra_secreta, palabra, letra):
    count = 0
    palabra = [x for x in palabra]
    palabra_secreta = [x for x in palabra_secreta]
    if letra in palabra_secreta:
        quant = palabra_secreta.count(letra)
        while count < quant:
            palabra[[i for i, n in enumerate(palabra_secreta) if n == letra][count]] = letra
            print(palabra)
            count += 1
    return "".join(palabra)


if __name__ == "__main__":
    palabra_secreta = "lepidoptero"
    palabra = "le_i_opter_"
    letra = "o"
    print(revisar_letra(palabra_secreta, palabra, letra))