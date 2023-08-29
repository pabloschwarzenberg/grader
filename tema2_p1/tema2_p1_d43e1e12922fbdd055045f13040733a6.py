# por favor escribe aquí tu función
def es_primo(numero):

    if numero == 2:
       return True
    elif numero == (-2):
        return False
    elif numero != 1:
        numero = abs(numero)
        d = numero
        d = d - 1
        while d > 1:

            if (numero % d) == 0:
                return False
            d = d - 1

        return True

    elif numero == 1: return False