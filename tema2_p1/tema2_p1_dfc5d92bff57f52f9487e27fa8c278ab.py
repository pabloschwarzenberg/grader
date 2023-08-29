# por favor escribe aquí tu función
def es_primo(numero):
    divisores = []
    for i in range(1, numero):
        if (numero % i == 0):
            divisores.append(i)
    if sum(divisores) == 1:
        primo = True
    else:
        primo = False
    return primo        