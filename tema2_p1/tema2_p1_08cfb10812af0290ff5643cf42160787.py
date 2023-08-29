# por favor escribe aquí tu función
def es_primo(numero):
    if numero<2:
        return False
    else:
        contador = 0
        for i in range(1,numero+1):
            if numero%i == 0:
                contador += 1
        if contador > 2:
            return False
        else:
            return True 
           