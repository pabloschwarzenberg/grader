# por favor escribe aquí tu función
def es_primo(numero):
    if numero == 1 or numero ==0:
        return False
    elif numero == 2:
        return True
    elif numero > 2:
        for i in range (2, numero):
            if numero % i ==0:
                return False
            elif numero % i != 0 and i == numero-1:
                return True

print (es_primo(11))
