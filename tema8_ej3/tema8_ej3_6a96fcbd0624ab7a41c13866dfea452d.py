import string

poema = """El hombre imaginario
vive en una mansión imaginaria
rodeada de árboles imaginarios
a la orilla de un río imaginario

De los muros que son imaginarios
penden antiguos cuadros imaginarios
irreparables grietas imaginarias
que representan hechos imaginarios
ocurridos en mundos imaginarios
en lugares y tiempos imaginarios

Todas las tardes tardes imaginarias
sube las escaleras imaginarias
y se asoma al balcón imaginario
a mirar el paisaje imaginario
que consiste en un valle imaginario
circundado de cerros imaginarios..."""


def get_word_count(string):
    return len(string.split())


def get_char_count(string):
    output_str = ""
    for char in string:
        if char.isalpha:
            output_str = output_str + char
    return len(output_str)


def get_avg_word_len(string):
    word_list = string.split()
    char_count = 0
    for word in word_list:
        for char in word:
            if char.isalpha():
                char_count = char_count + 1
    return char_count / len(word_list)  # may have to round


def get_space_count(string):
    space_count = 0
    for char in string:
        if char == " ":
            space_count = space_count + 1
    return space_count


def get_punctuation_count(string):
    count = 0
    for char in string:
        if char in [".", ",", ";"]:
            count += 1
    return count


def estadisticas_frase(s):
    return (
        get_word_count(s),
        get_char_count(s),
        get_avg_word_len(s),
        get_space_count(s),
        get_punctuation_count(s),
    )


if __name__ == "__main__":
    frase = input()
    print(estadisticas_frase(frase))
