# por favor escribe aquí tu función
def es_primo(numero):
    i = numero-1
    suma = 0
    while i >= 1:
        if numero%i == 0:
            suma += i
        i = i-1
    if suma == 1:
        return True
    else:
        return False

           