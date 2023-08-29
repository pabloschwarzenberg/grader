# por favor escribe aquí tu función
def es_primo(n):
    contador = 0
    for i in range(1, n+1):
        if n%i == 0:
            contador += 1
        if contador == 2:
            return False
        else:
            return True
print(es_primo(44))

           