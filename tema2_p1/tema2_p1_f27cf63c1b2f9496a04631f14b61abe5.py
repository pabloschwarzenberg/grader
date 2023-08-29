# por favor escribe aquí tu función
def es_primo(numero):
    i=2
    if numero == 1:
        return False
    while i < numero:
        if numero%i==0:
            return False
        i+=1
    return True     