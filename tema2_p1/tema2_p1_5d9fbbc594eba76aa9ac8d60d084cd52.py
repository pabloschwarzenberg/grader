# por favor escribe aquí tu función
def es_primo(numero):
    n = 1
    divisores = 0
    while n <= numero:
        mod = numero%n
        if mod == 0:
            divisores += 1
        n+=1
    if divisores == 2:
        return True
    else:
        return False