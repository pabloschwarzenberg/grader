import random

def find_all(string, substring):
    start = 0
    occurrences = []
    while True:
        a = string.find(substring, start)
        if a == -1:
            break
        else:
            occurrences.append(a)
        start = a+1
    return occurrences


def ocultar_letras(palabra, cantidad):
    for i in range(cantidad):
        a = random.randint(0, len(palabra) - 1)
        palabra_list = list(palabra)
        palabra_list.pop(a)
        palabra_list.insert(a, '_')
        palabra = ''.join(palabra_list)
    return palabra

def revisar_letra(palabra_secreta, palabra, letra):
    occurrences = find_all(palabra, '_')
    for index in occurrences:
        if letra == palabra_secreta[index]:
            palabra = palabra[0:index] + palabra[index:].replace('_', letra, 1)
    return palabra

if __name__ == "__main__":
    pass
