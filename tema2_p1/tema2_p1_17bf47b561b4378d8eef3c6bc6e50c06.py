def es_primo(numero):
    if numero < 2:
        return False
    for b in range(2, numero):
        if numero % b == 0:
            return False
    return True
    
numero = 1   
print(es_primo(numero))
