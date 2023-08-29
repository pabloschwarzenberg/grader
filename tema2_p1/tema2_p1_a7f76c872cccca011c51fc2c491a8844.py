# por favor escribe aquí tu función
def es_primo(numero):
    if numero==2 or numero==3: return True
    if numero%2==0 or numero<2: return False
    for i in range(3, int(numero**0.5)+1, 2):
        if numero%i==0:
            return False

    return True
print(es_primo(13))
           