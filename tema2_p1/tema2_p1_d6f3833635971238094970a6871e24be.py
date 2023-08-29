# por favor escribe aquí tu función
def es_primo(valor1):
    contador = 0
    for i in range(1, int(valor1)+1):
        if valor1 % i == 0:
            contador += 1
    if contador == 2:
        return True
    else:
        return False

