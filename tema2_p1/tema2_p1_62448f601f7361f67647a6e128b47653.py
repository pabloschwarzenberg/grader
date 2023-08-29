#Números Primos
def es_primo(numero):
    if numero == 0 or numero == 1 or numero == 2 or numero == 4:
        return False
    for algo in range(2, numero):
        if numero % algo == 0:
            return False
    return True