# por favor escribe aquí tu función
def es_primo(numero):
    i = 2
    if numero<2:
        return False
    if numero == 2:
        return True
    if numero==3: 
        return True
    while i < numero:
        if numero % i == 0:
            return False
        else:
            i += 1
        if i == (numero - 1):
            return True
