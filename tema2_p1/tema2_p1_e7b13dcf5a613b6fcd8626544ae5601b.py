# por favor escribe aquí tu función
def es_primo(numero):
    lista = [2,3,5,7,11]
    for i in lista:
        if numero == 1:
            return False
        elif numero%i == 0:
            return False
        elif numero/i < i:
            return True
        