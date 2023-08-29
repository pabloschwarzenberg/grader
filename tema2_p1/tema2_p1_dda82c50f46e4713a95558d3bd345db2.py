# por favor escribe aquí tu función
def es_primo(numero):
    divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            divisores += 1
    if divisores == 1:
        return True
    else:
        return False
           