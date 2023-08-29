# por favor escribe aquí tu función
def es_primo(numero):
    if numero < 2:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True
    
if __name__ == "__main__":
    numero = 17
    if es_primo(numero):
        print(str(numero) + "es un numero primo")
    else:
        print(str(numero) + "no es un número primo.")

