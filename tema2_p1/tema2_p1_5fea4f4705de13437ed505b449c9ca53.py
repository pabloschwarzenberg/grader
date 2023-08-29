# por favor escribe aquí tu funcion         
def es_primo(numero):
    if numero == 1:
        return False
    elif numero == 2:
        return True
    else:
        i = 2
        while(i<numero):
            resto = numero%i
            if resto == 0:
                return False
            else:
                i += 1
        return True   