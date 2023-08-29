# por favor escribe aquí tu función
numero=int(input("ponga un numero para evaluarlo:"))
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

if es_primo(numero):
    print(numero, "es primo")
else:
    print(numero, "no es primo")
