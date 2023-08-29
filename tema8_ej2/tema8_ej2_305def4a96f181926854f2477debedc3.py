import string as str
def buscartodas(a, b):
    indices = ''
    numero = 1
    for i in a:
        if i == b:
            if indices == '':
                numerostr = str(numero)
                indices += numerostr
                numero += 1
            else:
                indices += ''
                numerostr = str(numero)
                indices += numerostr
                numero += 1
        else:
            numero += 1

    return indices(a, b)

