# por favor escribe aquí tu función
def es_primo(numero):
    x=0
    for i in range(1, numero+1):
        if numero % i == 0:
            x += 1
    if x == 2:
        return True
    else:
        return False
numero=5
print(es_primo(numero))
           