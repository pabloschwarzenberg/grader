# por favor escribe aquí tu función
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True
numero = 17
if es_primo(numero):
    print(numero, "es primo")
else:
    print(numero, "no es primo")

           