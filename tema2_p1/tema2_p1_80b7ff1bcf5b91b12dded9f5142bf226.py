# por favor escribe aquí tu función
def es_primo(numero):
    if numero<2:
        return False
    elif numero==2:
        return TRUE
    else:
        for n in range (2,numero):
            if (numero%n)==0:
                return False
            elif (n==numero-1):
                return True 