# por favor escribe aquí tu función
def es_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True

# print(es_primo(1))
# print(es_primo(2))
# print(es_primo(3))
# print(es_primo(4))
# print(es_primo(5))
