# por favor escribe aquí tu función
def es_primo(a):
    contador = 0

    for i in range(1,a+1):
        if a % i == 0:
            contador += 1

    if contador == 2:
        return True

    else:
        return False

           