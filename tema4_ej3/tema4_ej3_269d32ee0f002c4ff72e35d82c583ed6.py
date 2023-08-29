def jerigonzo(palabra):
    palabra = list(palabra)
    vocales = 'AEIOUaeiou'
    palabra1 = ''

    for i in palabra:
        if i in vocales:
            palabra1 = palabra1 + i + 'p'
        palabra1 += i

    return palabra1

if __name__ == "__main__":
    pass
         