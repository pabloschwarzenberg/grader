# por favor escribe aquí tu función

## ENTRADA DE DATOS - PROCESO - SALIDA

def es_primo(Número):
    if Número < 2:
        return False
    for i in range(2, int(Número**0.5) + 1):
        if Número % i == 0:
            return False
    return True
           