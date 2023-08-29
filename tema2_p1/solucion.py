__version__ = "1.0"

def es_primo(numero):
    if numero==1:
        return False
    contador=2
    while contador<numero:
        if numero%contador==0:
            return False
        contador=contador+1
    return True