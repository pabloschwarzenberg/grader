from string import ascii_lowercase


def rot13(palabra):
    abet = list(ascii_lowercase) # len = 26, 14
    palabra = [x for x in palabra]
    count = 0
    for x in palabra:
        ind = abet.index(x)
        if ind + 13 > (len(abet) - 1):
            ind = abs(ind+13-(len(abet)))
        else:
            ind = ind + 13
        palabra[count] = abet[ind]
        count += 1
    return "".join(palabra)


           