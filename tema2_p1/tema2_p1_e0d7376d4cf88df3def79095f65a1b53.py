# por favor escribe aquí tu función
#Martín González B
def es_primo(numero):
    if numero > 1:
        for i in range(2,numero):
            if numero % i == 0:
                return False
            return True
    else:
        return False
           