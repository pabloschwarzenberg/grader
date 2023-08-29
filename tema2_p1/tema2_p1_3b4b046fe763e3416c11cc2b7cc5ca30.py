# por favor escribe aquí tu función
def es_primo(numero):
    if numero!=1:
        i=2
        while i<numero:
            if numero%i==0:
                i=numero+1
                return False
            else:
                i=i+1
        if i==numero:
            return True
    else:
        return False