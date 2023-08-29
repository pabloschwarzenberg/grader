# por favor escribe aquí tu función
def es_primo(numero):
    total = 0
    primo = False
    for i in range(numero-1):
        if numero%(i+1) == 0:
            total += (i+1)

    if total == 1:
        primo = True
        
    return primo 