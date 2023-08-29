# por favor escribe aquí tu función
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

num = int(input("Ingrese un numero: "))
print(es_primo(num))