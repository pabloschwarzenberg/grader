# por favor escribe aquí tu función
def es_primo(numero):
    if numero < 2:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True

def xd():
    numero = 7
    resultado = es_primo(numero)

    if resultado is True:
        print("su numero es primo")
    else:
        print("su numero no es primo")
xd()
     