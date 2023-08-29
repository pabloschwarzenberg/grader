# por favor escribe aquí tu función
def es_primo(numero):
    b = 2
    if numero == 1:
       return False
    while numero != b:
        if numero % b == 0:
            return False
        b += 1
    return True

           