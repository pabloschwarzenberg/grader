# por favor escribe aquí tu función
def es_primo(numero):
    primos = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
    if numero in primos:
        return True
    else:
        return False

num = 6
resultado = es_primo(num)
print(resultado)
