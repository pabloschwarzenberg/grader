# completa el código de la función
def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    
    return suma

def es_primo(numero):
    if suma_divisores(numero) == 1:
        return True
    else:
        return False


           