# por favor escribe aquí tu función
def es_primo(numero):
    if numero == 1:
        return False
    elif numero % 2:
        return True
    else:
        for i in range(2, numero):
            if numero % 1 == 0:
                return False
    return True
for i in range(1,211):
    print(i, es_primo(i))
