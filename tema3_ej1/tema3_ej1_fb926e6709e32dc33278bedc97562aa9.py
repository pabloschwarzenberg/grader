# completa el código de la funcióndef es_primo(numero):
def es_primo(numero): 
    if numero == 1:
        return False
    for i in range(2, numero):
        if (numero % i) == 0:
            return False
    return True

def suma_divisores(a):

    suma = 0
    for i in range(1,a):

        if a % i == 0:
            suma += i

    if es_primo(a)==False:
        return suma, False
    else:
        return suma, True

