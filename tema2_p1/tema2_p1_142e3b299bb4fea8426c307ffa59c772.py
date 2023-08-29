# por favor escribe aquí tu función
def es_primo(numero):
    if (numero <= 1):
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if (numero % i == 0):
            return False

    return True

numero = 17

if es_primo(numero):
    print("El número", numero, "es primo.")
else:
    print("El número", numero, "no es primo.")