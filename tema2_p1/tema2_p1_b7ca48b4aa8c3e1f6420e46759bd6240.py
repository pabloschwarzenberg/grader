def es_primo(numero):
    if numero<2:
        return False
    for j in range(2, numero):
        if numero%j==0:
            return False
    return True
print(es_primo(3))