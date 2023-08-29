def jerigonzo(palabra):
    vocales = ["a","e","i","o","u","á","é","í","ó","ú"]
    palabra = palabra.lower()
    for vocal in vocales:
        palabra = palabra.replace(vocal, vocal+"p"+vocal)

    return palabra

if __name__ == '__main__':
    print(jerigonzo("Hola, ¿comó estas?"))
    print(jerigonzo("soy un gato. muy misifus aaaa"))
         