# por favor escribe aquí tu función
def es_primo(numero):
    counter = 0
    for i in range(1, numero+1):
        if (numero%i) == 0:
            counter = counter+1

    if counter != 2:
        return False
    else:
        return True
           