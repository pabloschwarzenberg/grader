# por favor escribe aquí tu función
def es_primo(numero):
    if numero == 1:
        return False
    for i in range(1, numero+1):
        if numero%i == 0 and i != 1 and i != numero:
            return False
    return True



           