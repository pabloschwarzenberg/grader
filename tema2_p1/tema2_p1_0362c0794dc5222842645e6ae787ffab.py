# por favor escribe aquí tu función
#n-primos
def es_primo(x):
    numero = int(x)
    es_primo = True
    if numero == 1:
        es_primo = False

    for i in range(1, numero):
        if numero % i == 0:
            if i != 1:
                es_primo = False
                return es_primo
    return es_primo